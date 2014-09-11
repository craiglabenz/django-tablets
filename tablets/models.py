from __future__ import unicode_literals

# Django
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Template as DjangoTemplate, Context
from django.utils import module_loading

# 3rd Party
from annoying.fields import JSONField


class Template(models.Model):
    """
    The ultimate database-driven Django template experience.
    """

    DJANGO = 1
    JINJA2 = 2
    ENGINES = (
        (DJANGO, 'Django',),
        (JINJA2, 'Jinja2',),
    )

    JINJA2_NOT_FINISHED = "Error: Jinja2 templates do not handle inheritance correctly."

    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    template_engine = models.IntegerField(choices=ENGINES, default=DJANGO, verbose_name="Template Engine")
    parent = models.ForeignKey('self', blank=True, null=True,
        help_text="Select another template this template should extend.", related_name="children")
    default_context = JSONField(default="{}", blank=True, verbose_name="Default Context")

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
            # TODO: Finish this
            raise NotImplementedError(self.JINJA2_NOT_FINISHED)

            if not hasattr(settings, "JINJA2_TEMPLATE_CLASS"):
                raise NotImplementedError("Must set ``JINJA2_TEMPLATE_CLASS`` to the dotted import path of a Jinja2 template class before Tablets can interface with Jinja2!")
            return module_loading.import_by_path(dotted_path=settings.JINJA2_TEMPLATE_CLASS)

    def get_absolute_url(self):
        """Used for admin previewing"""
        return reverse("admin:tablets_template_render", args=(self.pk,))

    def as_template(self):
        if self.template_engine in [Template.DJANGO]:
            return self.template_engine_class(self.get_content())
        elif self.template_engine in [Template.JINJA2]:
            # TODO: Finish this
            raise NotImplementedError(self.JINJA2_NOT_FINISHED)

    def render(self, context={}):
        return self.as_template().render(Context(context))

    def render_default(self):
        return self.as_template().render(Context(self.default_context))

    def add_block(self, name="content", content=""):
        return TemplateBlock.objects.create(template=self, name=name, content=content)

    def get_content(self):
        content = self.content
        if self.parent:
            # If there's a parent, add the {% extends `parent-name` %}
            # tag at the top
            content = """{%% extends "%s" %%}""" % (self.parent.name,)

            for block in self.blocks.all():
                content += "\n\n{%% block %s %%}%s{%% endblock %s %%}" % (block.name, block.content, block.name,)

        return content


class TemplateBlock(models.Model):
    """
    How Templates influence their Parent.
    """
    template = models.ForeignKey(Template, related_name="blocks")
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Template Block"
        verbose_name_plural = "Template Blocks"
        unique_together = (
            ("template", "name",),
        )

    def __unicode__(self):
        return "%s: %s" % (self.template.__unicode__(), self.name,)
