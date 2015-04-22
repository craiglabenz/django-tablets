# django-tablets

* `tablets` is a database templating layer for Django.
    * It works out of the box with regular Django templates, and requires only installing `django-jinja` to support Jinja2 templates.
* `django-ace` is used to provide a nice in-browser editing experience.

> Note that `tablets` is frozen at Django <= 1.7.*, as Django 1.8's refactor of the template layer makes DB-and-J2 nature of this app completely unnecessary.


### Preview
![Admin preview](https://raw.githubusercontent.com/craiglabenz/django-tablets/master/media/admin-change-form.png "Optional Title")


### Installation

Install using `pip`:

```py
pip install tablets
```

Add `tablets` and `mptt` to your `INSTALLED_APPS` setting:
```py
INSTALLED_APPS = (
    ...
    'mptt',
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

Tablets reloads templates from the database each time. To turn off this functionality and only reload templates after an application reload, add this to your settings file:
```py
# Defaults to True
JINJA2_SHOULD_RELOAD_DB_TEMPLATES = False
```


### Django-Ace in the Admin
By default, `tablets` uses `django-ace` to use the great [AceWidget](http://ace.c9.io/build/kitchen-sink.html) for admin in-browser editing.

To disable or tweak these settings, adjust the following settings (default values shown):
```py
USE_ACE_WIDGET = True
ACE_MODE = "twig"  # Provides syntax highlighting closest to Django/Jinja2 templates
ACE_THEME = "chrome"
ACE_WIDTH = "80%"  # Defaults to 100%
ACE_HEIGHT = "500px"  # Defaults to 350px
```


### Usage

First, enter some templates into your Database.
```py
parent = Template.objects.create(name="Site Base", content="""
    <h1>{% block hero %}Hello, World!{% endblock hero %}</h1>

   {% block body %}
       <p>This is a message from your friends at <code>Tablet</code>!</p>
   {% endblock body %}
""")
landing_page_template = Template.objects.create(
    name="Landing Page",
    parent=parent,
    content="""{% block body %}OVERRIDDEN FROM CHILD TEMPLATE!{% endblock body %}"""
)
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
