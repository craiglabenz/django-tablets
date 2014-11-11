# django-tablets

`tablets` is a database templating layer for Django. It works out of the box with regular Django templates, and requires only installing `django-jinja` to support Jinja2 templates.

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
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'tablets.loaders.DatabaseLoader',
)
```

## Jinja2 Support

If you want to use Jinja2 templates, adjust the above config like so:
```py
TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
    'tablets.loaders.DatabaseLoader',
)

INSTALLED_APPS = (
    ...
    'django_jinja',
    'tablets',
)

JINJA2_TEMPLATE_CLASS = "django_jinja.base.Template"
JINJA2_LOADER = "tablets.j2.loaders.Jinja2DatabaseOrFileLoader"
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
