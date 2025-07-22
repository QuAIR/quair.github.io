# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'QuAIR-Platform'
copyright = '2025, Tengxiang Lin, QuAIR. All Rights Reserved.'
author = 'Tengxiang Lin'
release = 'beta'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'nbsphinx',  # For Markdown and Jupyter notebook support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'site', 'mkdocs_src']


# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
# pygments_dark_style = 'monokai'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']
html_logo = '_static/avocado-icon.svg'
html_favicon = '_static/avocado-icon.svg'

# -- Theme options -----------------------------------------------------------
html_theme_options = {
    "github_url": "https://github.com/QuAIR",
    "nav_links": [
        {
            "title": "Home",
            "url": "index",
        },
        {
            "title": "QuAIRKit",
            "url": "https://quairkit.com/QuAIRKit/",
        },
        {
            "title": "QRLab", 
            "url": "https://quairkit.com/QRLab/",
        },
        {
            "title": "QuICK",
            "url": "quick/index",
        },
        {
            "title": "Research",
            "url": "research",
        },
    ],
}

# MyST parser configuration
# myst_enable_extensions = [
#     "colon_fence",
#     "deflist",
#     "dollarmath",
#     "html_admonition",
#     "html_image",
#     "linkify",
#     "replacements",
#     "smartquotes",
#     "substitution",
#     "tasklist",
# ]

# MathJax configuration
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_css_files = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {
    "**": [],
}
#         "sidebar-search.html",
#     ]
# }
#     "smartquotes",
#     "substitution",
#     "tasklist",
# ]

# MathJax configuration
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_css_files = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
# html_sidebars = {
#     "**": [
#         "sidebar-tree.html",
#         "sidebar-search.html",
#     ]
# }
