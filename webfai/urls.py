from django.conf.urls import url

from . import views
#app_name = 'webfai'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<machine_pk>[0-9]+)/wakeup/$', views.wakeup, name='wakeup'),
    url(r'^(?P<machine_pk>[0-9]+)/modify/$', views.modify, name='modify'),
    url(r'^(?P<machine_pk>[0-9]+)/clone/$', views.clone, name='clone'),
    url(r'^(?P<machine_pk>[0-9]+)/delete/$', views.delete, name='delete'),
]

