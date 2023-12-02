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
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'lagrangian diags'
copyright = f'{datetime.datetime.now().year}, The OceanParcels Team'
author = 'The OceanParcels Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "myst_parser",
    "nbsphinx",
    "numpydoc",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The root document.
root_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# numpydoc support
# ----------------
numpydoc_class_members_toctree = False  # https://stackoverflow.com/a/73294408

# full list of numpydoc error codes: https://numpydoc.readthedocs.io/en/latest/validation.html
numpydoc_validation_checks = {
    "GL05",
    "GL06",
    "GL07",
    "GL10",
    "PR05",
    "PR10",
    "RT02",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "logo": "lagrangian-diag-logo.png",
    "use_edit_page_button": True,
    "github_url": "https://github.com/OceanParcels/Lagrangian_diag",
    "icon_links": [
        {
            "name": "Conda Forge",
            "url": "https://anaconda.org/conda-forge/parcels",  # required
            "icon": "fa-solid fa-box",
            "type": "fontawesome",
        }
    ]
}
