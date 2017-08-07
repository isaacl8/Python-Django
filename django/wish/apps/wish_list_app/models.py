from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def validate(self, post):
        name = post['name']
        username = post['username']
        password = post['password']
        passconf = post['passconf']
        errors = []

        if not name:
            errors.append('username field is required')
        if len(name) < 3:
            errors.append('username must be at least 3 characters long')
        if not username:
            errors.append('username field is required')
        if len(username) < 3:
            errors.append('username must be at least 3 characters long')
        check_user = self.filter(name=name).filter(username=username)
        if check_user:
            errors.append('username already exists in the database')
        if not password:
            errors.append('password is required')
        elif len(password) < 8:
            errors.append('password must be at least 8 characters long')
        elif not password == passconf:
            errors.append('password and confirmation fields must match')

        return errors

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wish(models.Model):
    item = models.CharField(max_length=40)
    added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
