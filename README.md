# django-tablets

* `tablets` is a database templating layer for Django.
    * It works out of the box with regular Django templates, and requires only installing `django-jinja` to support Jinja2 templates.
* `django-ace` is used to provide a nice in-browser editing experience.


### Preview
![Admin preview](https://raw.githubusercontent.com/craiglabenz/django-tablets/master/media/admin-change-form.png "Optional Title")


### Installation

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

### Jinja2 Support

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

### Django-Ace in the Admin
By default, `tablets` uses `django-ace` to use the great [AceWidget](http://ace.c9.io/build/kitchen-sink.html) to for admin in-browser editing.

To disable or tweak these settings, adjust the following settings (default values shown):
```py
USE_ACE_WIDGET = True
ACE_MODE = "twig"  # Provides syntax highlighting closest to Django/Jinja2 
templates
ACE_THEME = "chrome"
```
>The `django-ace` JavaScript works best with DOM elements that are in place on page ready, so behavior can be a little funny with additional inlines. It is suggested to add one `TemplateBlock` per form save to get around this.


### Usage

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
