#from django.conf.urls import url,patterns,include
from django.conf.urls import url,include

from . import views
#app_name = 'webfai'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<machine_pk>[0-9]+)/wakeup/$', views.wakeup, name='wakeup'),
    url(r'^(?P<machine_pk>[0-9]+)/modify/$', views.modify, name='modify'),
    url(r'^(?P<pk>[0-9]+)/modified/$', views.modified.as_view(), name='modified'),
    url(r'^(?P<machine_pk>[0-9]+)/clone/$', views.clone, name='clone'),
    url(r'^(?P<machine_pk>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<pk>[0-9]+)/deleted/$', views.deleted.as_view(), name='deleted'),
    url(r'^(?P<pk>[0-9]+)/details/$', views.details.as_view(), name='details'),
]

