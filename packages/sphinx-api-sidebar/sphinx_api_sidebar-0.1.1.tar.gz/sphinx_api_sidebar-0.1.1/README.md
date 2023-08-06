# Sphinx API Sidebar

A Sphinx extension for displaying any generated static API documentation in a sidebar.

## Overview

This Sphinx extension allows you to include and display static API documentation (e.g., `JavaDoc`, `Doxygen`) in the sidebar of your Sphinx documentation. It updates the `html_context` with the API documentation paths, which can then be used in the API sidebar template.

This extension serves as an immediate workaround to make Sphinx consume API docs from various languages without building additional extensions.

## Installation

To install the `sphinx-api-sidebar` extension, you can use pip:

```sh
pip install sphinx-api-sidebar
```

## Usage
1. To enable the sphinx-api-sidebar extension in your Sphinx documentation project, add it to the extensions list in your conf.py file:

```python
extensions = [
    'sphinx_api_sidebar',
    # Other extensions...
]
```

2. To use a custom command to generate your API documentation or specify different directories, you can set the api_docs_generator configuration value in your conf.py file:

```python
api_docs_generators = [
  {
    'command': '<your_api_docs_build_command_1>',
    'outputs': [
            {
                'name': '<generated_api_doc_name_1>',
                'path': '<path_to_generated_api_doc_1>'
            },
            {
                'name': '<generated_api_doc_name_2>',
                'path': '<path_to_generated_api_doc_2>'
            },
            # ...
        ]
  },
  {
    'command': '<your_custom_build_command_2>',
    'outputs': [
            {
                'name': '<generated_api_doc_name_3>',
                'path': '<path_to_generated_api_doc_3>'
            },
            # ...
        ]
  },
  # more groups of generated api docs
]
```

Replace <your_custom_build_command_*>, <generated_api_doc_name_*>, and <path_to_generated_api_doc_*> with the appropriate values for your project.


3. To make the different api documentation show up in the sidebar, you will need to copy the `api_docs_sidebar.html` template file from the `sphinx_api_sidebar/templates` folder of the installed package to your Sphinx project's _templates folder. Alternatively, you can create a new file in your project's _templates folder with the following content:

```html
{% if api_docs %}
  <h3>{{ _('API Documentation') }}</h3>
  <ul style="list-style-type: none;">
    {%- for item in api_docs %}
      <li style="margin-bottom: 10px;"><a href="{{ pathto('_static/api-docs/{}'.format(item), 1) }}">{{ item }}</a></li>
    {%- endfor %}
  </ul>
{% endif %}
```

4. Update your `conf.py` file to include the `api_docs_sidebar.html` template in the html_sidebars configuration:

```python
html_sidebars = {
    '**': [
        # ... other sidebars ...
        'api_docs_sidebar.html',
    ]
}
```
