from __future__ import unicode_literals

# Django
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Template as DjangoTemplate, Context
from django.utils import module_loading

# 3rd Party
from annoying.fields import JSONField
from mptt.models import MPTTModel, TreeForeignKey

try:
    import django_jinja
    from django_jinja.base import env
except ImportError as e:
    django_jinja = None


class Template(MPTTModel):
    """
    The ultimate database-driven Django template experience.
    """

    DJANGO = 1
    JINJA2 = 2
    ENGINES = (
        (DJANGO, 'Django',),
        (JINJA2, 'Jinja2',),
    )

    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    template_engine = models.IntegerField(choices=ENGINES, default=DJANGO, verbose_name="Template Engine")
    parent = TreeForeignKey('self', blank=True, null=True,
        help_text="Select another template this template should extend.", related_name="children")
    default_context = JSONField(default="{}", blank=True, verbose_name="Default Context")

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __unicode__(self):
        return self.name

    @property
    def template_engine_class(self):
        if self.template_engine == self.DJANGO:
            return DjangoTemplate
        elif self.template_engine == self.JINJA2:
            if not django_jinja:
                from .j2.exceptions import DjangoJinjaNotInstalled
                raise DjangoJinjaNotInstalled

            return module_loading.import_by_path(dotted_path=settings.JINJA2_TEMPLATE_CLASS)

    def get_absolute_url(self):
        """Used for admin previewing"""
        return reverse("admin:tablets_template_render", args=(self.pk,))

    def as_template(self):
        if self.template_engine in [Template.DJANGO]:
            return self.template_engine_class(self.get_content())
        elif self.template_engine in [Template.JINJA2]:
            if django_jinja:
                # Make sure the loader is initialized. django-jinja doesn't automatically
                # handle the initialization in Django 1.7
                if not env.loader:
                    env.initialize_template_loader()

                return env.from_string(self.get_content())
            else:
                from .j2.exceptions import DjangoJinjaNotInstalled
                raise DjangoJinjaNotInstalled

    def render(self, context={}):
        if self.template_engine in [Template.DJANGO]:
            return self.as_template().render(Context(context))
        else:
            return self.as_template().render(context)

    def render_default(self):
        return self.as_template().render(Context(self.default_context))

    def get_content(self):
        content = self.content
        if self.parent:
            # If there's a parent, add the {% extends `parent-name` %}
            # tag at the top
            content = """{{% extends "{0}" %}}\n\n{1}""".format(self.parent.name, content)

        return content
