# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

from urllib.parse import quote


def linkcode_resolve(domain, info):
    # print(f"domain={domain}, info={info}")
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = quote(info["module"].replace(".", "/"))
    if not filename.startswith("tests"):
        filename = "src/" + filename
    if "fullname" in info:
        anchor = info["fullname"]
        anchor = "#:~:text=" + quote(anchor.split(".")[-1])
    else:
        anchor = ""

    # github
    result = "https://<github>/<user>/<repo>/blob/master/%s.py%s" % (filename, anchor)
    # print(result)
    return result


# -- Project information -----------------------------------------------------

project = "lagrangian diags"
copyright = f"{datetime.datetime.now().year}, The OceanParcels Team"
author = "The OceanParcels Team"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.linkcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "myst_parser",
    "nbsphinx",
    "numpydoc",
    "sphinx_design",
]

nbsphinx_thumbnails = {
    "tutorials/GKDE_method01": "_static/GKDE_01_thumbnail.png",
    "tutorials/GKDE_method02": "_static/GKDE_02_thumbnail.png",
    "tutorials/absolute_distance_method01": "_static/lagrangian-diag-logo.png",
    "tutorials/center_of_mass_dispersion_method01": "_static/center_of_mass_dispersion_method01_thumbnail.png",
    "tutorials/center_of_mass_displacement_method01": "_static/center_of_mass_displacement_method01_thumbnail.png",
    "tutorials/cumulative_distance_method01": "_static/cumulative-distance-thumbnail.png",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The root document.
root_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# numpydoc support
# ----------------
numpydoc_class_members_toctree = False  # https://stackoverflow.com/a/73294408

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "logo": {
        "image_light": "lagrangian-diag-logo.png",
        "image_dark": "lagrangian-diag-logo.png",
    },
    "use_edit_page_button": True,
    "github_url": "https://github.com/OceanParcels/Lagrangian_diags",
}

html_context = {
    "github_user": "OceanParcels",
    "github_repo": "Lagrangian_diags",
    "github_version": "main",
    "doc_path": "docs",
}

html_css_files = [
    "custom.css",
]
