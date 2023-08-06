import sphinx_rtd_theme
import os
import sys
# from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))



# def setup(app):
#     app.add_config_value('recommonmark_config', {
#         'auto_toc_tree_section': 'Contents',
#     }, True)
#     app.add_transform(AutoStructify)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'insta-captions'
copyright = '2023, David Cendejas'
author = 'David Cendejas'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = [sphinx_rtd_theme.get_html_theme_path()]
