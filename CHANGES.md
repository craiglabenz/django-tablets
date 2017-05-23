Changelog
=========

0.1.0 (2014/09/10)
------------------
 - Initial commit


0.2.0 (2014/11/11)
------------------
 - Adds Jinja2 support


0.2.1 (2014/11/11)
------------------
 - Removes gnarly `print`


0.3.0 (2014/11/11)
------------------
 - Adds `django-ace` to the admin


0.3.2 (2014/11/13)
------------------
 - Adds initial migrations


0.3.3 (2014/11/20)
------------------
 - Fixes Jinaj2 rendering bug


0.4.2 (2014/11/21)
------------------
 - Adds mptt, removes "TemplateBlock" model


 0.4.6 (2015/12/08)
 ------------------
  - Various DB-vs-filesystem customizations moved to run-time code instead of top of level Django settings


0.5.0 (2016/10/06)
------------------
 - Drops requirement for `django_jinja`
 - Updates to support `django>=1.8`
 - Drops support `django<=1.7`

0.6.0 (2016/10/07)
------------------
 - Removes historical usage of `django-annoying`, since it isn't even maintained enough to be migrated away from. This makes `tablets==0.6.0` incompatible for upgrade from earlier versions (without manual work altering your database), as earlier migrations are re-written.

0.6.1 (2017/05/23)
------------------
 - Uses django.template.Template.name attr when casting from Tablet record
