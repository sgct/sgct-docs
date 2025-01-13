import os
import sys

# The way Sphinx handles the path during the evaluation of the conf.py is a bit strange
# so we have to add the current folder or else the `import` statement will fail
sys.path.append(os.path.abspath("."))
from generatedocs import generate_docs

##########################################################################################
#                                     CUSTOMIZATION                                      #
##########################################################################################
# This is the branch on the SGCT repository from which the documentation will be built.
# Change this to a different branch to try a local branch before committing.
# OBS: No other value than `master` should ever be committed to the master branch of the
#      docs repository
SGCT_BRANCH = "master"

# If this value is specified, instead of cloning SGCT from the main repository using the
# branch provided above, instead use a local copy of the repository.
# OBS: No other value than the empty string should ever be committed to the master branch
#      of the docs repository
LOCAL_SGCT_FOLDER = "sgct-checkout"



# Generate the documentation files based on the JSON schema file located in the main SGCT
# repository. This saves us from duplicating that documentation.
generate_docs(SGCT_BRANCH, LOCAL_SGCT_FOLDER)


###
# Global Settings
###
needs_sphinx = "4.0"

project = "SGCT"
author = "SGCT community"
project_copyright = "2012-2025, SGCT community"

# Update with every new release
version = release = os.getenv("READTHEDOCS_VERSION", "4.0.0")

extensions = [
  "myst_parser",
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.duration",
  "sphinxcontrib.jquery",
  "sphinxcontrib.luadomain",
  "sphinxcontrib.mermaid"
]

keep_warnings = True



###
# Content
###
source_encoding = "utf-8-sig"
exclude_patterns = [
  "README.md",
  ".venv"
]
root_doc = "index"
primary_domain = "cpp"
autosectionlabel_prefix_document = True
pygments_style = "default"
pygments_dark_style = "monokai"

myst_enable_extensions = {
  "colon_fence",
  "fieldlist"
}
myst_heading_anchors = 3



###
# HTML output
###
html_theme = "furo"
html_static_path = ["_static"]
html_theme_options = {
  # No written project title in the sidebar
  "sidebar_hide_name": True,

  # Make the edit button in the top right appear
  "source_repository": "https://github.com/SGCT/SGCT-Docs/",
  "source_branch": "master",
  "source_directory": "/",

  # Set CSS Variables. The dark theme inherits all light variables
  "light_css_variables": {
    "font-stack--monospace": "Source Code Pro Light, monospace",
  },

  # Add custom items in the footer
  "footer_icons": [
    {
        "name": "GitHub",
        "url": "https://github.com/SGCT/SGCT",
        "html": "",
        "class": "fa-brands fa-solid fa-github fa-2x"
    },
  ],

  "light_logo": "logo.png",
  "dark_logo": "logo-inverted.png"
}
html_title = "SGCT documentation"
html_short_title = "SGCT"

html_favicon = "assets/images/icon.png"

# JavaScript files that are added into the generated documentation
html_js_files = [

]

# CSS files that are added into the generated documentation
html_css_files = [
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css"
]

# These folders are copied to the documentation's HTML output

# html_extra_path = ["robots.txt"]
