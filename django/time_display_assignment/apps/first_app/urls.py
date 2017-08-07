from django.conf.urls import url
from . import views
import datetime

urlpatterns = [
    url(r'^$', views.index)
]
