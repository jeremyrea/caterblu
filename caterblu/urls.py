import source.views.views

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', source.views.views.index, name='index'),
    url(r'^api/price', source.views.views.price, name='price'),
    staticfiles_urlpatterns()
]
