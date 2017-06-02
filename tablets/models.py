from __future__ import unicode_literals

# Django
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Template as DjangoTemplate, Context
from django.utils import module_loading

# 3rd Party
from jsonfield import JSONField
from mptt.models import MPTTModel, TreeForeignKey


try:
    import jinja2
    # Local Apps
    from tablets.j2.loaders import DatabaseLoader
    env = jinja2.Environment(loader=DatabaseLoader(
        should_reload_db_templates=getattr(settings, 'SHOULD_RELOAD_JINJA2_TEMPLATES', True)
    ))

except ImportError as e:
    jinja2 = None


class Template(MPTTModel):
    """
    The ultimate database-driven Django template experience.
    """

    DJANGO = 1
    JINJA2 = 2
    ENGINES = (
        (DJANGO, 'Django',),
    )

    if jinja2:
        ENGINES = (
            (DJANGO, 'Django',),
            (JINJA2, 'Jinja2',)
        )

    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    template_engine = models.IntegerField(choices=ENGINES, default=DJANGO, verbose_name="Template Engine")
    parent = TreeForeignKey('self', blank=True, null=True,
        help_text="Select another template this template should extend.", related_name="children")
    default_context = JSONField(default=dict, blank=True, verbose_name="Default Context",
        help_text="Does not work so well for Jinja2 templates, which throw exceptions for missing values. This can make things "
        "tough if your template relies on functions.")

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __unicode__(self):
        return self.name + ''

    def __str__(self):
        return self.name

    def get_default_context(self):
        if self.parent_id:
            context = self.parent.get_default_context()
            context.update(self.default_context)
        else:
            context = self.default_context.copy()
        return context

    @property
    def source(self):
        """
        Pass-thru to Django template attr
        """
        return self.content

    @property
    def template_engine_class(self):
        if self.template_engine == self.DJANGO:
            return DjangoTemplate
        elif self.template_engine == self.JINJA2:

            return module_loading.import_by_path(dotted_path=settings.JINJA2_TEMPLATE_CLASS)

    def get_absolute_url(self):
        """Used for admin previewing"""
        return reverse("admin:tablets_template_render", args=(self.pk,))

    def as_template(self):
        if self.template_engine in [Template.DJANGO]:
            template = self.template_engine_class(self.get_content(), name=self.name)
            template.tablet = self
            return template
        elif self.template_engine in [Template.JINJA2]:
            if jinja2:
                if not env.loader:
                    env.initialize_template_loader()

                template = env.from_string(self.get_content())
                template.tablet = self
                return template
            else:
                from tablets.j2.exceptions import Jinja2NotInstalled
                raise Jinja2NotInstalled

    def render(self, context=None):
        context = context or {}
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
