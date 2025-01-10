from git import Repo
from jinja2 import Environment, FileSystemLoader
import json
import re
import os
import glob

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

def is_paged_type(type):
  return any(entry["path"] == type for entry in Individual_Pages)

def extract_data(schema, location):
  original_location = location

  # Remove the prefix indicating the root
  if location.startswith("#/"):
    location = location[2:]

  local_schema = schema

  # Dig down through the tree
  while "/" in location:
    loc = location.split("/", 1)[0]
    location = location.split("/", 1)[1]

    if loc not in local_schema:
      raise Exception(f"Could not find '{loc}' in the schema. Full location: {original_location}")

    local_schema = local_schema[loc]

  if location != "" and location not in local_schema:
      raise Exception(f"Could not find '{location}' in the schema")

  if location == "":
    item = local_schema
  else:
    item = local_schema[location]

  if "properties" in item:
    for k in item["properties"]:
      # Resolve $defs
      if "$ref" in item["properties"][k]:
        ref = item["properties"][k]["$ref"]
        description = ""
        if "description" in item["properties"][k]:
          description = item["properties"][k]["description"]
        item["properties"][k] = extract_data(schema, ref).copy()
        item["properties"][k]["description"] = description
        item["properties"][k]["reference_type"] = ref
        continue

      if "oneOf" in item["properties"][k]:
        for i in range(len(item["properties"][k]["oneOf"])):
          v = item["properties"][k]["oneOf"][i]
          if "$ref" in v:
            ref = v["$ref"]
            description = ""
            if "description" in v:
              description = v["description"]
            item["properties"][k]["oneOf"][i] = extract_data(schema, ref).copy()
            item["properties"][k]["oneOf"][i]["description"] = description
            item["properties"][k]["oneOf"][i]["reference_type"] = ref

  return item


def markdownify(value):
  def replace_match(match):
    word = match.group()
    for page in Individual_Pages:
      if page["path"] == f"#/$defs/{word.lower()}":
        prefix = page.get("prefix") or ""
        return f"[{word}](/users/configuration/{prefix}/{word.lower()})"
    return word

  def replace_url(match):
    url = match.group()
    return f"[link]({url})"

  if value:
    t = re.sub(r"\b[A-Z][a-zA-Z0-9]*\b", replace_match, value)
    t = re.sub(r"\bhttps?://[^\s.,]+(?:\.[^\s.,]+)*(?<!\.)", replace_url, t)
    return t
  else:
    return None


def friendly_type(value):
  def handle_array(p):
    items = p["items"]
    if "type" in items:
      return f"array of {friendly_type(items["type"])}s"
    if "$ref" in items:
      t = items["$ref"].split("/")[-1]
      return f"array of [{t.capitalize()}]({t})s"

  def handle_boolean(p):
    return "boolean"

  def handle_integer(p):
    if "enum" in p:
      return ", ".join([str(x) for x in p["enum"]])
    if "minimum" in p and "maximum" in p:
      if p["minimum"] == p["maximum"]:
        return f"integer equal to {p["minimum"]}"
      else:
        return f"integer between {p["minimum"]} and {p["maximum"]}"
    if "minimum" in p:
      if p["minimum"] == 0:
        return f"non-negative integer"
      elif p["minimum"] == 1:
        return f"positive integer"
      else:
        return f"integer min {p["minimum"]}"
    if "maximum" in p:
      return f"integer max {p["maximum"]}"

    return "integer"

  def handle_number(p):
    if "enum" in p:
      return ", ".join([str(x) for x in p["enum"]])
    if "minimum" in p and "maximum" in p:
      if p["minimum"] == p["maximum"]:
        return f"number equal to {p["minimum"]}"
      else:
        return f"number between {p["minimum"]} and {p["maximum"]}"
    if "exclusiveMinimum" in p:
      if p["exclusiveMinimum"] == 0:
        return "positive number"
      else:
        return f"number bigger than {p["exclusiveMinimum"]}"
    if "minimum" in p:
      if p["minimum"] == 0:
        return f"non-negative number"
      elif p["minimum"] == 1:
        return f"positive number"
      else:
        return f"number min {p["minimum"]}"
    if "maximum" in p:
      return f"number max {p["maximum"]}"

    return "number"

  def handle_object(p):
    if "reference_type" in p:
      t = p["reference_type"].split("/")[-1]
      match t:
        case "ivec2": return "[ivec2](/users/configuration/index.md#ivec2)"
        case "ivec3": return "[ivec3](/users/configuration/index.md#ivec3)"
        case "ivec4": return "[ivec4](/users/configuration/index.md#ivec4)"
        case "vec2": return "[vec2](/users/configuration/index.md#vec2)"
        case "vec3": return "[vec3](/users/configuration/index.md#vec3)"
        case "vec4": return "[vec4](/users/configuration/index.md#vec4)"
        case "color": return "[color](/users/configuration/index.md#color)"
        case "orientation": return "[orientation](/users/configuration/index.md#orientation)"
        case _:
          if is_paged_type(p["reference_type"]):
            for page in Individual_Pages:
              if page["path"] == p["reference_type"]:
                prefix = page.get("prefix")
                if prefix:
                  return f"[{t.capitalize()}](/users/configuration/{prefix}/{t})"
                else:
                  return f"[{t.capitalize()}](/users/configuration/{t})"
            assert(False)
          else:
            return "object"
    else:
      return "object"

  def handle_string(p):
    if "enum" in p:
      return ", ".join(p["enum"])
    if "const" in p:
      return f"string = {p["const"]}"
    if "minLength" in p and "maxLength" in p:
      return f"string between {p["minLength"]} and {p["maxLength"]}"
    if "minLength" in p:
      if p["minLength"] == 1:
        return f"non-empty string"
      else:
        return f"string min {p["minLength"]}"
    if "maxLength" in p:
      return f"string max {p["maxLength"]}"

    return "string"


  if "type" in value:
    match value["type"]:
      case "array":    return handle_array(value)
      case "boolean":  return handle_boolean(value)
      case "integer":  return handle_integer(value)
      case "number":   return handle_number(value)
      case "object":   return handle_object(value)
      case "string":   return handle_string(value)
      case _:          return value["type"]
  elif "oneOf" in value:
    return "one of the following"
  else:
    return value


def composite_type(value):
  if "reference_type" in value:
    Reference_Types = [
"#/$defs/orientation", "#/$defs/mat4", "#/$defs/vec2", "#/$defs/vec3", "#/$defs/vec4", "#/$defs/ivec2", "#/$defs/ivec3", "#/$defs/ivec4", "#/$defs/color", "#/$defs/projectionquality"
    ]
    is_reference_type = value["reference_type"] in Reference_Types
    return not is_reference_type and not is_paged_type(value["reference_type"])
  elif "type" in value:
    return value["type"] == "object"
  else:
    return False


def array_composite_type(value):
  if value.get("type") == "array":
    return composite_type(value.get("items"))
  else:
    return False



def generate_docs(branch, local_folder):
  environment = Environment(loader=FileSystemLoader("templates"))
  environment.filters["markdownify"] = markdownify
  environment.filters["friendly_type"] = friendly_type
  environment.tests["composite_type"] = composite_type
  environment.tests["array_composite_type"] = array_composite_type


  # Clone the repository if necessary
  if local_folder == "":
    def print_progress(op_code, cur_count, max_count=None, message=""):
      print(message)

    local_folder = "sgct-checkout"

    print("Cloning repository")
    repo = Repo.init(local_folder)

    # Create a new remote if there isn't one already created
    origin = repo.remotes[0] if len(repo.remotes) > 0 else None
    if not origin:
      print("No remote origin found. Creating SGCT remote...")
      origin = repo.create_remote("origin", "https://github.com/SGCT/SGCT")

    print(f"Fetching SGCT... this might take a while")
    origin.fetch(progress=print_progress, depth=1)

    git = repo.git()
    git.checkout(f"origin/{branch}", "--", "sgct.schema.json")

  schema_file = f"{local_folder}/sgct.schema.json"
  with open(schema_file, "r") as file:
    schema = json.load(file)
  template = environment.get_template("configuration.html.jinja")

  def write_configuration(title, schema, schema_path, folder_prefix = ""):
    data = extract_data(schema, schema_path)

    # Find examples
    part = schema_path.split("/")[-1]
    examples = None
    if os.path.exists(f"assets/configs/examples/{part}"):
      examples = glob.glob(f"assets/configs/examples/{part}/*.json")

    doc = template.render(data=data, title=title, examples=examples)
    with open(f"users/configuration/{folder_prefix}/{title.lower().replace(" ", "")}.md", "w") as f:
      f.write(doc)

  for page in Individual_Pages:
    if "prefix" in page:
      write_configuration(page["name"], schema, page["path"], page["prefix"])
    else:
      write_configuration(page["name"], schema, page["path"])



# For debugging purposes, make this file executable directly with default values
if __name__ == "__main__":
  generate_docs("master", "sgct-checkout")
