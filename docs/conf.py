# docs/conf.py

import os
import sys
#import sphinx_rtd_theme

# -- Path setup --------------------------------------------------------------

# Add the project's root directory to sys.path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'test Zaveza Arhiv'
author = 'Your Name or Organization'
release = '0.1'  # Version number

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google-style docstrings
    'sphinx.ext.viewcode',
]

# Templates path
templates_path = ['_templates']

# List of patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Use the Read the Docs theme
#html_theme = 'sphinx_rtd_theme'
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Static files path (for custom CSS, etc.)
html_static_path = ['_static']

# -- Extensions configuration ------------------------------------------------

# Configuration for autodoc (automatically document modules)
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'show-inheritance': True,
}

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
