from __future__ import unicode_literals
from django.db import models
# Create your models here. They need to be singular

class UserManager(models.Manager):
    def validate(self, post):
        username = post['username']
        password = post['password']
        passconf = post['passconf']
        errors = []

        if not username:
            errors.append('username field is required')
        if len(username) < 8:
            errors.append('username must be at least 8 characters long')
        if len(username) > 16:
            errors.append('username cannot be more than characters long')
        check_user = self.filter(username=username)
        if check_user:
            errors.append('username already exists in the database')
        if not password:
            errors.append('password is required')
        elif len(password) < 8:
            errors.append('password must be at least 8 characters long')
        elif not password == passconf:
            errors.append('password and confirmation fields must match')

        return errors


class User(models.Model):
    #element name =
    #treat like an ERD table
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
