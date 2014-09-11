from __future__ import unicode_literals

# Django
from django.core.urlresolvers import reverse
from django.db import models
from django.template.base import Template as DjangoBaseTemplate
from django.template.loader import get_template
from django.test import TestCase
from django.test.utils import override_settings

# Local Apps
from tablets.models import Template


class TemplateTester(TestCase):

    def setUp(self):
        super(TemplateTester, self).setUp()

        # Both will default to Django templates
        self.parent_template = Template.objects.create(name="Parent Tmpl", parent=None, content="Hello{% block content %}, {{ name }}{% endblock content %}!", default_context='{"name": "World"}')
        self.child_template = Template.objects.create(name="Child Tmpl", parent=self.parent_template, default_context='{"name": "Marco Polo"}')
        self.child_template.add_block(content=" dearest ole pal, {{ name }}")

    def test_get_content(self):
        self.assertEquals(self.parent_template.get_content(), "Hello{% block content %}, {{ name }}{% endblock content %}!")
        self.assertIn("dearest ole pal, {{ name }}", self.child_template.get_content())
        self.assertIn("{%% extends '%s' %%}" % (self.parent_template.name,), self.child_template.get_content())

    def test_parent_render(self):
        self.assertEquals(self.parent_template.render_default(), "Hello, World!")
        self.assertEquals(self.parent_template.render(), "Hello, !")

    def test_child_render(self):
        self.assertEquals(self.child_template.render_default(), "Hello dearest ole pal, Marco Polo!")
        self.assertEquals(self.child_template.render(), "Hello dearest ole pal, !")

    def test_template_loading(self):
        tmpl = get_template(self.parent_template.name)
        self.assertTrue(isinstance(tmpl, DjangoBaseTemplate))


class ViewTester(TestCase):

    def setUp(self):
        super(ViewTester, self).setUp()
        self.landing_page_template = Template.objects.create(name="Landing Page", content="""<a href="{% url \'dummy-view\' pk=1 %}">Hai!</a>""")

    def test_view_using_tablet_template(self):
        # Get the URL we set up for just this purpose
        url = reverse("dummy-view", kwargs={"pk":1})

        # Request that View
        resp = self.client.get(url)

        # The template includes a URL tag that happens
        # to resolve to... the same URL!
        self.assertIn(url, resp.content)

