"""Sphinx configuration."""
project = "Enrichify"
author = "Dallan Quass"
copyright = "2022, Dallan Quass"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
