from __future__ import unicode_literals

# Django
from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from django.template.loaders import app_directories
from django.utils import six

default_loader_dirs = (app_directories.app_template_dirs +
                       tuple(settings.TEMPLATE_DIRS))

# 3rd Party
from .exceptions import Jinja2NotInstalled

# Local Apps
from ..models import Template

try:
    import jinja2
    from jinja2.loaders import FileSystemLoader
except ImportError as e:
    jinja2 = None


try:
    import django_jinja
    from django_jinja.base import env
except ImportError as e:
    django_jinja = None


class Jinja2DatabaseOrFileLoader(FileSystemLoader):
    """
    This guy talks to the database and returns something Jinja2 wants.
    """
    def __init__(self, searchpath=None, encoding='utf-8'):
        searchpath = searchpath or default_loader_dirs
        if isinstance(searchpath, six.string_types):
            searchpath = [searchpath]
        self.searchpath = list(searchpath)
        self.encoding = encoding

    def get_source(self, environment, template):
        if not jinja2:
            raise Jinja2NotInstalled

        def uptodate():
            return True

        try:
            tmpl = Template.objects.get(name=template, template_engine=Template.JINJA2)
            return tmpl.get_content().decode(self.encoding), template, uptodate
        except Template.DoesNotExist:
            return super(Jinja2DatabaseOrFileLoader, self).get_source(environment, template)


class DjangoJinja2DatabaseLoader(BaseLoader):
    """
    Django's ``get_template`` function talks to this function.
    """
    is_usable = True
    load_template_source = None

    def load_template(self, template_name, template_dirs=None):
        return env.get_template(template_name), template_name
