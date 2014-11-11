from __future__ import unicode_literals

# Django
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# 3rd Party
from django_ace import AceWidget

# Local Apps
from .models import Template, TemplateBlock


class AceWidgetMixin(object):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if getattr(settings, "USE_ACE_WIDGET", True) and db_field.name == "content":
            kwargs["widget"] = AceWidget(mode=getattr(settings, "ACE_MODE", "twig"), theme=getattr(settings, "ACE_THEME", "chrome"))

        return super(AceWidgetMixin, self).formfield_for_dbfield(db_field, **kwargs)


class TemplateBlockInline(AceWidgetMixin, admin.TabularInline):
    extra = 1
    model = TemplateBlock


class TemplateAdmin(AceWidgetMixin, admin.ModelAdmin):
    inlines = [TemplateBlockInline]

    @property
    def admin_view_info(self):
        return "%s_%s" % (self.model._meta.app_label, self.model._meta.model_name,)

    def get_urls(self):
        urls = super(TemplateAdmin, self).get_urls()
        my_urls = [
            url(r'^(.+)/render/', self.render, name="%s_render" % self.admin_view_info,),
        ]
        return my_urls + urls

    def render(self, request, obj_id):
        template = get_object_or_404(Template, pk=obj_id)
        return HttpResponse(template.render())


admin.site.register(Template, TemplateAdmin)
