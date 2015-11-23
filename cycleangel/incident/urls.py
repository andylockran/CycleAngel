from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new incident'),
]
