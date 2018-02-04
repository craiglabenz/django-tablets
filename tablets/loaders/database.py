from __future__ import unicode_literals

# Django
from django.template import Origin, TemplateDoesNotExist
from django.template.loaders.base import Loader

# Local Apps
from tablets.models import Template


class Loader(Loader):

    is_usable = True

    def __call__(self, template_name, template_dirs=None):
        return self.load_template(template_name, template_dirs)

    def load_template(self, template_name, template_dirs=None):
        """
        Wraps the Django or Jinja2 template loading particulars
        """
        try:
            template = Template.objects.get(name=template_name)
            return template.as_template(), template_name
        except Template.DoesNotExist:
            raise TemplateDoesNotExist(template_name)

    def get_template_sources(self, template_name, template_dirs=None):
        return [Origin(
            name=template_name,
            template_name=template_name,
            loader=self
        )]

    def get_contents(self, origin):
        template, name = self.load_template(origin.template_name)
        return template.source
