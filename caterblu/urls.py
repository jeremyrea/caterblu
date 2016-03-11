import source.views.views

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', source.views.views.index, name='index'),
    staticfiles_urlpatterns()
]
