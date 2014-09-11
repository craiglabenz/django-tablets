from __future__ import unicode_literals

# Django
from django.template.loader import BaseLoader
from django.template import TemplateDoesNotExist

# Local Apps
from .models import Template


class DatabaseLoader(BaseLoader):

    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        try:
            template = Template.objects.get(name=template_name)
            return template.get_content(), template_name
        except Template.DoesNotExist:
            raise TemplateDoesNotExist(template_name)
