from __future__ import unicode_literals

# Django
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import TemplateView

# Local Apps
from core.views import DummyView


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jinja-parent/$', TemplateView.as_view(template_name="Jinja 2 Parent"), name="jinja2-parent"),
    url(r'^jinja-child/$', TemplateView.as_view(template_name="Jinja 2 Child"), name="jinja2-child"),
    url(r'^jinja-file/$', TemplateView.as_view(template_name="marco.jinja"), name="marco"),
    url(r'^django-template/$', TemplateView.as_view(template_name="polo.html"), name="django-template"),
    url(r'^for-reversing-in-templates/(?P<pk>[\d]+)/$', DummyView.as_view(), name="dummy-view")
]

urlpatterns += staticfiles_urlpatterns()