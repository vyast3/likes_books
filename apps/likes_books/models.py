from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
      first_name = models.CharField(max_length=255,blank=True)
      last_name = models.CharField(max_length=255,blank=True)
      email = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)


class Book(models.Model):
      name = models.CharField(max_length=255,blank=True)
      desc = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      uploader = models.ForeignKey(User, related_name = "uploaded_books")
      liked_users = models.ManyToManyField(User, related_name = "liked_books")
      

