from __future__ import unicode_literals


class Jinja2NotInstalled(Exception):
    message = "Error: Must install jinja2 to use Jinja2 templates."


class DjangoJinjaNotInstalled(Exception):
    message = "Error: Must install django-jinja to use Jinja2 templates."
