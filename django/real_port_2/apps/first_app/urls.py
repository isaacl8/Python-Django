from django.conf.urls import url
from . import views
urlpatterns = [
    # goes to the index function in views.py
    url(r'^$', views.index),
    # goes to the projects function in views.py
    url(r'^projects$', views.projects),
    # goes to the about function in views.py
    url(r'^about$', views.about),
    # goes to the test function in views.py
    url(r'^testimonials$',views.testimonials)
]
