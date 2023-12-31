###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
BUILDDIR = '_build'
author = 'Derek'
comments_config = {'hypothesis': False, 'utterances': False}
copybutton_only_copy_prompt_lines = False
copybutton_prompt_text = ''
copybutton_remove_prompts = False
copyright = '2023'
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', '.github',
                    'README.md', 'Thumbs.db', '__pycache__', '_build']
execution_allow_errors = False
execution_excludepatterns = []
execution_in_temp = False
execution_timeout = 30
extensions = ['sphinx_togglebutton',
              'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe',
              'sphinx_comments', 'sphinx_external_toc',
              'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme',
              'sphinx_jupyterbook_latex']
external_toc_exclude_missing = False
external_toc_path = '_toc.yml'
html_baseurl = 'http://problog-template.simply-logical.space/'
html_css_files = ['problog-book-template.css']
html_extra_path = ['README.md', 'LICENCE', 'CNAME', '.nojekyll']
html_favicon = 'src/img/wikidata.svg'
html_logo = 'src/img/wikidata.svg'
html_sourcelink_suffix = ''
html_static_path = ['_static']
html_theme = 'sphinx_book_theme'
html_theme_options = {'search_bar_text': 'Search this book...',
                      'launch_buttons': {'notebook_interface': 'classic','thebe': True}, 'path_to_docs': '',
                      'repository_url':'https://github.com/scls-cs/cs2023',
                      'repository_branch': 'jb',
                      'google_analytics_id': 'G-BZGV6J36FT', 'extra_navbar':
                          '', 'extra_footer': 'This book is for teaching '
                                              'Computer Science at <a '
                                              'href="https://scls.org.cn">SCLS</a>. \n',
                      'home_page_in_toc': True, 'announcement': '',
                      'use_repository_button': True,
                      'use_edit_page_button': True, 'use_issues_button': True}
html_title = '信息技术'
jupyter_cache = ''
jupyter_execute_notebooks = 'cache'
language = 'en'
latex_engine = 'pdflatex'
myst_enable_extensions = ['colon_fence', 'dollarmath', 'linkify']
myst_url_schemes = ['mailto', 'http', 'https']
nb_custom_formats = {'.py': ['jupytext.reads', {'fmt': 'py:percent'}]}
nb_output_stderr = 'show'
numfig = True
numfig_format = {'figure': 'Figure %s'}
numfig_secnum_depth = 1
pygments_style = 'sphinx'
sphinx_problog_code_directory = 'src/code/'
sphinx_problog_execution_server_url = 'https://verne.cs.kuleuven.be/problog/api/'
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
use_multitoc_numbering = True

import os

on_rtd = os.environ.get("READTHEDOCS") == "True"

if on_rtd:
    html_baseurl = os.environ.get("READTHEDOCS_OUTPUT", "")
    if html_baseurl:
        html_baseurl = os.path.join(html_baseurl, "html")
    else:
        html_baseurl = BUILDDIR
else:
    html_baseurl = BUILDDIR

html_theme_path = [html_baseurl]
