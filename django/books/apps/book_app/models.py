from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    published_date = models.DateTimeField(auto_now_add = True)
    in_print = models.BooleanField(default=True)
