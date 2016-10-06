# Django
from django.template.backends.base import BaseEngine
from django.template.exceptions import TemplateDoesNotExist

# Local Apps
from tablets.models import Template


class TabletBackend(BaseEngine):

    def get_template(self, template_name):
        try:
            template = Template.objects.get(name=template_name)
        except Template.DoesNotExist as e:
            raise TemplateDoesNotExist(e.args, backend=self)
        else:
            return template.as_template()