from __future__ import unicode_literals

# Django
from django.template.loader import BaseLoader
from django.template import TemplateDoesNotExist

# Local Apps
from .models import Template


try:
    import django_jinja
    from django_jinja.base import env
    env.initialize()
except ImportError as e:
    django_jinja = None


class DatabaseLoader(BaseLoader):

    is_usable = True

    def __call__(self, template_name, template_dirs=None):
        return self.load_template(template_name, template_dirs)

    def load_template(self, template_name, template_dirs=None):
        """
        Wraps the Django or Jinja2 template loading particulars
        """
        print "DatabaseLoader is fetching", template_name
        try:
            template = Template.objects.get(name=template_name)
            if template.template_engine == template.DJANGO:
                return self.load_django_template_source(template, template_name)
            else:
                return self.load_jinja2_template_source(template, template_name)
        except Template.DoesNotExist:
            raise TemplateDoesNotExist(template_name)

    def load_django_template_source(self, template, template_name):
        return template.get_content(), template_name

    def load_jinja2_template_source(self, template, template_name):
        if django_jinja:
            template = env.from_string(template.get_content())
            return template, template_name
        else:
            from .j2.exceptions import DjangoJinjaNotInstalled
            raise DjangoJinjaNotInstalled
