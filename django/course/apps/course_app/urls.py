from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/$', views.process),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^remove/(?P<id>\d+)$', views.remove)

# (?P<id>\d+)
]
