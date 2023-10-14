import os


###
# Global Settings
###
needs_sphinx = "4.0"

project = "SGCT"
author = "SGCT community"
project_copyright = "2012-2023, SGCT community"

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
  "README.md"
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
    "font-stack--monospace": "Source Code Pro, monospace",
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
html_title = f'SGCT documentation ({version})'
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
