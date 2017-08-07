from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$',views.dashboard, name="dashboard"),
    url(r'^secrets$',views.popular_secret, name="popular_secrets"),
    url(r'^secrets/create$',views.create_secret, name="create_secret"),
    url(r'^secrets/(?P<id>\d+)/like$',views.like, name="like"),
    url(r'^secrets/(?P<id>\d+)/delete$',views.delete, name="delete")
]
