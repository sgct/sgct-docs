from git import Repo
from jinja2 import Environment, FileSystemLoader
import json
import re
import os
import glob
import shutil

# This variable contains the Schema that we are currently working on. It is a global
# variable as (a) there is only one schema we are working with and (b) the Jinja filters
# need access to the schema to be able to resolve potential $def references and this is
# cleaner than carrying an extra variable around through the whole process
global Schema

# These are the pages that are created on their own. Other objects that are defined in the
# schema file will be described locally. Objects that have their own page are referenced
# via a link instead
Individual_Pages = [
  { "name": "Cluster",                      "path": "" },
  { "name": "Node",                         "path": "#/$defs/node" },
  { "name": "Window",                       "path": "#/$defs/window" },
  { "name": "Viewport",                     "path": "#/$defs/viewport", },
  { "name": "Scene",                        "path": "#/$defs/scene" },
  { "name": "User",                         "path": "#/$defs/user" },
  { "name": "Settings",                     "path": "#/$defs/settings" },
  { "name": "Capture",                      "path": "#/$defs/capture" },
  { "name": "Device",                       "path": "#/$defs/device" },
  { "name": "Tracker",                      "path": "#/$defs/tracker" },
  { "name": "Cubemap Projection",           "path": "#/$defs/cubemapprojection",         "prefix": "projection" },
  { "name": "Cylindrical Projection",       "path": "#/$defs/cylindricalprojection",     "prefix": "projection" },
  { "name": "Equirectangular Projection",   "path": "#/$defs/equirectangularprojection", "prefix": "projection" },
  { "name": "Fisheye Projection",           "path": "#/$defs/fisheyeprojection",         "prefix": "projection" },
  { "name": "Planar Projection",            "path": "#/$defs/planarprojection",          "prefix": "projection" },
  { "name": "ProjectionPlane",              "path": "#/$defs/projectionplane",           "prefix": "projection" },
  { "name": "Spherical Mirror Projection",  "path": "#/$defs/sphericalmirrorprojection", "prefix": "projection" },
  { "name": "Texture Mapped Projection",    "path": "#/$defs/texturemappedprojection",   "prefix": "projection" }
]

# These are types that we use a "built-in types that are defined separately. So whenever
# we encounter these in a documentation we just want to treat then as given and not dig
# down into them whenever using them
BuiltIn_Types = [
  { "name": "orientation", "def": "#/$defs/orientation" },
  { "name": "mat4",        "def": "#/$defs/mat4" },
  { "name": "vec2",        "def": "#/$defs/vec2" },
  { "name": "vec3",        "def": "#/$defs/vec3" },
  { "name": "vec4",        "def": "#/$defs/vec4" },
  { "name": "ivec2",       "def": "#/$defs/ivec2" },
  { "name": "ivec3",       "def": "#/$defs/ivec3" },
  { "name": "ivec4",       "def": "#/$defs/ivec4" },
  { "name": "color",       "def": "#/$defs/color" },
]

# Finds the provided `location` in the `schema`. The location can be a `/` delimited
# string where this function will traverse the schema and returns the referenced object.
# If the value could not be found, an `Exception` is raised
def find_value(location):
  global Schema
  # Store the original location for better error messages
  original_location = location

  # Remove the prefix indicating the root
  if location.startswith("#/"):
    location = location[2:]

  schema = Schema

  # Dig down through the tree until no separator is left
  while "/" in location:
    loc, location = location.split("/", 1)

    if loc not in schema:
      raise Exception(f"Could not find '{loc}'. Full location: {original_location}")
    schema = schema[loc]

  if location != "" and location not in schema:
    raise Exception(f"Could not find '{original_location}' in the schema")

  if location == "":
    return schema
  else:
    return schema[location]


# This filter revieves a description text and automatically converts some links into
# Markdown links. These can be to other individual pages or links to external webpages
# that will automatically get shortened
def markdownify(value):
  if not value:
    return ""

  def replace_match(match):
    word = match.group()
    for page in Individual_Pages:
      if page["path"] == f"#/$defs/{word.lower()}":
        prefix = page.get("prefix") or ""
        return f"[{word}](/users/configuration/{prefix}/{word.lower()})"
    return word
  t = re.sub(r"\b[A-Z][a-zA-Z0-9]*\b", replace_match, value)

  def replace_url(match):
    return f"[link]({match.group()})"
  t = re.sub(r"\bhttps?://[^\s.,]+(?:\.[^\s.,]+)*(?<!\.)", replace_url, t)

  return t


# This filter extracts the type from a schema definition. The function is able to resolve
# a $ref reference to another part of the same schema file and convert different types
# into a human-readable format.
# In case references get resolved, the resulting value contains a `reference_value` key
# that indicates the original reference name
def extract_type(value):
  def handle_array(p):
    subtype = extract_type(value["items"])
    return f"array of {subtype}s"

  def handle_numerical(p, number_type):
    if "enum" in p:
      return ", ".join([str(x) for x in p["enum"]])

    if "minimum" not in p and "exclusiveMinimum" not in p and "maximum" not in p and "exclusiveMaximum":
      return number_type

    min = p.get("minimum", p.get("exclusiveMinimum"))
    max = p.get("maximum", p.get("exclusiveMaximum", "{math}`\infty`"))
    start = "[" if "minimum" in p else "("
    end = "]" if "maximum" in p else ")"
    return f"{number_type}  {start}{min}, {max}{end}"

  def handle_string(p):
    if "enum" in p:
      return ", ".join(p["enum"])
    if "const" in p:
      const = p["const"]
      return f"string = \"{const}\""
    if "minLength" in p and "maxLength" in p:
      minLength = p["minLength"]
      maxLength = p["maxLength"]
      return f"string between {minLength} and {maxLength} characters"
    if "minLength" in p:
      if p["minLength"] == 1:
        return f"non-empty string"
      else:
        minLength = p["minLength"]
        return f"string min length {minLength}"
    if "maxLength" in p:
      maxLength = p["maxLength"]
      return f"string max length {maxLength}"

    return "string"

  def handle_object(p):
    if "type_reference" in p:
      t = p["type_reference"].split("/")[-1]

      if any(entry["name"] == t for entry in BuiltIn_Types):
        # If it is a built-in type, we have manually written some documentation for it and
        # just need to create a link here
        return f"[{t}](/users/configuration/types.md#{t})"
      else:
        if any(entry["path"] == p["type_reference"] for entry in Individual_Pages):
          # If it is a base type that has its own page, we can create a link to that page
          for page in Individual_Pages:
            if page["path"] == p["type_reference"]:
              prefix = page.get("prefix")
              if prefix:
                return f"[{t.capitalize()}](/users/configuration/{prefix}/{t})"
              else:
                return f"[{t.capitalize()}](/users/configuration/{t})"
        else:
          # This is a type we have created a $def entry for but only to keep the schema
          # file more manageble. We don't want to create a separate page for it and
          # instead the documentation will contain copies of it
          return "object"
    else:
      # This is just an object definition without any referencing going on
      return "object"


  if "$ref" in value:
    ref = value["$ref"]
    value = find_value(ref)
    value["type_reference"] = ref

  if "type" in value:
    match value["type"]:
      case "array":    return handle_array(value)
      case "boolean":  return "boolean"
      case "integer":  return handle_numerical(value, "integer")
      case "number":   return handle_numerical(value, "number")
      case "object":   return handle_object(value)
      case "string":   return handle_string(value)
      case _:          assert(False)
  elif "oneOf" in value:
    return "one of the following"
  else:
    return value


# This filter takes an object and if it is a reference to another place in the
# schema document, it will resolve that link and infill the value
def resolve_reference(value):
  if "$ref" in value and not any(entry["path"] == value["$ref"] for entry in Individual_Pages):
    return find_value(value["$ref"])
  else:
    return value


# This filter takes the path to an example JSON file and returns the corresponding
# image file. If no such image file exists, and Exception is raised
def image_from_example(value):
  assert os.path.exists(value), f"Configuration file {value} did not exist"

  pre, ext = os.path.splitext(value)
  image = f"{pre}.png"

  assert ext == ".json", f"image_from_example called on non-configuration path {value}"
  assert os.path.exists(image), f"Image {image} for configuration {value} did not exist"
  return image


# This filter determines whether we want to locally drill into the properties of an object
# while creating the documentation. We only want to do this if the `value` is an object
# and we don't have already created a documentation for, which is only the case for
# "built-in" types that we manually documented and types for which we are creating
# individual pages
def composite_type(value):
  if "$ref" in value and not any(entry["path"] == value["$ref"] for entry in Individual_Pages):
    value = find_value(value["$ref"])

  if "type" in value and value["type"] != "object":
    return False

  if "type_reference" in value:
    is_builtin_type = any(entry["def"] == value["type_reference"] for entry in BuiltIn_Types)
    is_paged_type =  any(entry["path"] == value["type_reference"] for entry in Individual_Pages)
    return not is_builtin_type and not is_paged_type
  elif "type" in value:
    return value["type"] == "object"
  else:
    return False


# This filter does the same operation as #composite_type but for arrays instead.
def array_composite_type(value):
  if value.get("type") == "array":
    return composite_type(value.get("items"))
  else:
    return False


# Generate the documentation Markdown files. If `local_folder` is not specified, we check
# out the SGCT repository to get access to the `sgct.schema.json`` which contains all of
# the primary documentation. This schema file will then be read and converted into the
# Markdown files that we serve as the documentation
def generate_docs(branch, local_folder = ""):
  environment = Environment(loader=FileSystemLoader("templates"))
  environment.filters["markdownify"] = markdownify
  environment.filters["extract_type"] = extract_type
  environment.filters["resolve_reference"] = resolve_reference
  environment.filters["image_from_example"] = image_from_example
  environment.tests["composite_type"] = composite_type
  environment.tests["array_composite_type"] = array_composite_type
  template = environment.get_template("configuration.html.jinja")


  # Clone the repository if necessary
  if local_folder == "":
    def print_progress(op_code, cur_count, max_count=None, message=""):
      print(message)

    local_folder = "sgct_checkout"

    print("Cloning repository")
    repo = Repo.init(path=local_folder, mkdir=True)

    # Create a new remote if there isn't one already created
    origin = repo.remotes[0] if len(repo.remotes) > 0 else None
    if not origin:
      print("No remote origin found. Creating SGCT remote...")
      origin = repo.create_remote("origin", "https://github.com/SGCT/SGCT")

    print(f"Fetching SGCT... this might take a while")
    origin.fetch(progress=print_progress, depth=1)

    git = repo.git()
    git.checkout(f"origin/{branch}", "--", "sgct.schema.json")


  # Load the schema file
  schema_file = f"{local_folder}/sgct.schema.json"
  with open(schema_file, "r") as file:
    global Schema
    Schema = json.load(file)


  # Create the individual pages
  for page in Individual_Pages:
    title = page["name"]
    schema_path = page["path"]
    prefix = page.get("prefix") or ""

    # For debugging purposes if only a single page should be generated
    # if title != "Cubemap Projection":
      # continue

    component = schema_path.split("/")[-1] or "cluster"

    data = find_value(schema_path)
    examples = glob.glob(f"assets/configs/examples/{component}/*.json")
    examples = [example.replace(os.sep, "/") for example in examples]
    doc = template.render(data=data, title=title, examples=examples)
    with open(f"users/configuration/{prefix}/{component}.md", "w") as f:
      f.write(doc)



# For debugging purposes, make this file executable directly with default values
# if __name__ == "__main__":
  # generate_docs("master", "")
