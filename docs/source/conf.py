project = 'SatIST'
copyright = '2025, LLNL'
author = 'LLNL'
release = 'v3.0'

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']



extensions = [
    'sphinx_rtd_theme',
    "sphinxcontrib.bibtex",
    'sphinx_automodapi.automodapi',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.graphviz',
    'sphinx_automodapi.smart_resolver',
]
automodapi_inheritance_diagram = True
graphviz_output_format = 'svg' 

bibtex_bibfiles = ["refs.bib"]
bibtex_reference_style = "author_year"

html_theme = "sphinx_rtd_theme"
