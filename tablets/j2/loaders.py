from __future__ import unicode_literals

# Django
from django.conf import settings
# from django.template import TemplateDoesNotExist
from django.template.loaders.base import Loader
from django.template.utils import get_app_template_dirs
from django.utils import six

from jinja2.exceptions import TemplateNotFound

# 3rd Party
from tablets.j2.exceptions import Jinja2NotInstalled

try:
    import jinja2
    from jinja2.loaders import BaseLoader
except ImportError as e:
    jinja2 = None


class DatabaseLoader(BaseLoader):
    """
    This guy talks to the database and returns something Jinja2 wants.
    """
    def __init__(self, encoding='utf-8', should_reload_db_templates=True):
        self.encoding = encoding
        self.should_reload_db_templates = should_reload_db_templates

    def uptodate(self):
        return not self.should_reload_db_templates

    def get_source(self, environment, template):
        if not jinja2:
            raise Jinja2NotInstalled
        # Local Apps
        from tablets.models import Template

        try:
            tmpl = Template.objects.get(name=template, template_engine=Template.JINJA2)
            content = tmpl.get_content()

            # This code runs in Python 2.7, but not 3.x
            if hasattr(content, 'decode'):
                content = content.decode(self.encoding)

            return (content, template, self.uptodate,)
        except Template.DoesNotExist:
            raise TemplateNotFound(template)
