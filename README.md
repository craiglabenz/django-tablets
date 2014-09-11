# django-tablets

`tablets` is a database templating layer for Django. It works out of the gate with regular Django templates, with Jinja2 support in progress.

## Installation

Install using `pip`:

```py
pip install tablets
```

Add `tablets` to your `INSTALLED_APPS` setting:
```py
INSTALLED_APPS = (
    ...
    'tablets',
)
```

Add the `tablets` template loader to your `TEMPLATE_LOADERS` setting:
```py
TEMPLATE_LOADERS = (
    ...
    'tablets.loaders.DatabaseLoader',
)
```

## Usage

First, enter some templates into your Database.
```py
parent = Template.objects.create(name="Site Base", content="""
    <h1>{% block hero %}Hello, World!{% endblock hero %}</h1>

   {% block body %}
       <p>This is a message from your friends at <code>Tablet</code>!</p>
   {% endblock body %}
""")
landing_page_template = Template.objects.create(name="Landing Page", parent=parent)
landing_page_template.add_block(name="body", content="OVERRIDDEN FROM CHILD TEMPLATE!")
```

```py
# views.py
from django.views.generic.base import TemplateView

class MyView(TemplateView):
    # The ``tablet`` template loader will know how to find
    # this as if it were a file on disk like normal templates
    template_name = "Landing Page"
```

And that's it! When you hit a URL that registers to `MyView`, the contents of the "Landing Page" template will be rendered out of the database!