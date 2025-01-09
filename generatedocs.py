from git import Repo
from jinja2 import Environment, FileSystemLoader
import json
import re
import os
import glob

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




# Tracker/Devices/offset and Tracker/Devices/transformation
# don't have a proper type without this code, but we don't want to resolve _all_
# $refs recursively. Need something smarter here

#       if item["properties"][k]["type"] == "object":
#         item["properties"][k] = extract_data(schema, f"{original_location}/properties/{k}").copy()
#         continue
#
#       if item["properties"][k]["type"] == "array":
#         item["properties"][k] = extract_data(schema, f"{original_location}/properties/{k}/items").copy()
#         continue

  # if "items" in item:
  #   assert(item["type"] == "array")
  #   if "$ref" in item["items"]:
  #       ref = item["items"]["$ref"]
  #       description = ""
  #       if "description" in item["properties"][k]:
  #         description = item["properties"][k]["description"]
  #       item["items"] = extract_data(schema, ref).copy()
  #       item["items"]["description"] = description
  #       item["items"]["reference_type"] = ref

  return item



def create_human_type(data):
  def handle_array(p):
    items = p["items"]
    if "type" in items:
      return f"array of {create_human_type(items["type"])}s"
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
        case _:       return f"[{t.capitalize()}]({t})"
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


  def handle_data(data):
    if "type" in data:
      human_type = data["type"]
      match data["type"]:
        case "array":    human_type = handle_array(data)
        case "boolean":  human_type = handle_boolean(data)
        case "integer":  human_type = handle_integer(data)
        case "number":   human_type = handle_number(data)
        case "object":   human_type = handle_object(data)
        case "string":   human_type = handle_string(data)
      data["human_type"] = human_type

      if data["type"] == "object":
        # Recurse down
        if "properties" in data:
          for k in data["properties"]:
            handle_data(data["properties"][k])

      if data["type"] == "array" and "type" in data["items"] and data["items"]["type"] == "object":
        handle_data(data["items"])
        data["human_items"] = data["items"]

  # CONTINUE HERE;  WHEN GOING INTO ARRAY TYPE "items" IT DOES NOT HAVE A 'properties' SO
  # THE TOP IF STATEMENT DOESN"T DO ANYTHING

  if "properties" in data:
    for k in data["properties"]:
      handle_data(data["properties"][k])

  return data


def generate_docs(branch, local_folder):
  environment = Environment(loader=FileSystemLoader("templates"), trim_blocks=False, lstrip_blocks=False)

  def markdownify(value):
    def replace_match(match):
      word = match.group()
      filename = f"users/configuration/{word.lower()}.md"
      if os.path.isfile(filename):
        return f"[{word}]({word.lower()})"
      return word

    def replace_url(match):
      url = match.group()
      return f"[link]({url})"

    if not value:
      return value

    # Regular expression to match capitalized words
    links_pattern = r"\b[A-Z][a-zA-Z0-9]*\b"
    text = re.sub(links_pattern, replace_match, value)

    url_pattern = r"\bhttps?://[^\s.,]+(?:\.[^\s.,]+)*(?<!\.)"
    text = re.sub(url_pattern, replace_url, text)

    return text

  def show_all_attrs(value):
      res = []
      for k in dir(value):
          res.append('%r %r\n' % (k, getattr(value, k)))
      return '\n'.join(res)

  environment.filters["markdownify"] = markdownify
  environment.filters["show_all_attrs"] = show_all_attrs


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
    data = create_human_type(extract_data(schema, schema_path))

    # Find examples
    part = schema_path.split("/")[-1]
    examples = None
    if os.path.exists(f"assets/configs/examples/{part}"):
      examples = glob.glob(f"assets/configs/examples/{part}/*.json")

    doc = template.render(data=data, title=title, examples=examples)
    with open(f"users/configuration/{folder_prefix}/{title.lower().replace(" ", "")}.md", "w") as f:
      f.write(doc)

  write_configuration("Cluster", schema, "")
  write_configuration("Node", schema, "#/$defs/node")
  write_configuration("Window", schema, "#/$defs/window")
  write_configuration("Viewport", schema, "#/$defs/viewport")
  write_configuration("Scene", schema, "#/$defs/scene")
  write_configuration("User", schema, "#/$defs/user")
  write_configuration("Settings", schema, "#/$defs/settings")
  write_configuration("Capture", schema, "#/$defs/capture")
  write_configuration("Device", schema, "#/$defs/device")
  write_configuration("Tracker", schema, "#/$defs/tracker")

  write_configuration("Cubemap Projection", schema, "#/$defs/cubemapprojection", "projection")
  write_configuration("Cylindrical Projection", schema, "#/$defs/cylindricalprojection", "projection")
  write_configuration("Equirectangular Projection", schema, "#/$defs/equirectangularprojection", "projection")
  write_configuration("Fisheye Projection", schema, "#/$defs/fisheyeprojection", "projection")
  write_configuration("Planar Projection", schema, "#/$defs/planarprojection", "projection")
  write_configuration("ProjectionPlane", schema, "#/$defs/projectionplane", "projection")
  write_configuration("Spherical Mirror Projection", schema, "#/$defs/sphericalmirrorprojection", "projection")
  write_configuration("Texture Mapped Projection", schema, "#/$defs/texturemappedprojection", "projection")




if __name__ == "__main__":
  generate_docs("master", "sgct-checkout")
