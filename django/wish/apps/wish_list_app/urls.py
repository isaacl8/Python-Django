from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^dashboard$',views.dashboard),
    # url(r'^wish_item/(?P<id>\w+)$',views.wish_items),
    # url(r'^wish_item/(?P<id>\w+)$',views.create),


]
