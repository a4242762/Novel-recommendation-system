# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Novel(models.Model):
    img_src = models.TextField(blank=True, null=True)
    book_name = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    book_state = models.TextField(blank=True, null=True)
    book_infomation = models.TextField(blank=True, null=True)
    book_one_title = models.TextField(blank=True, null=True)
    book_two_title = models.TextField(blank=True, null=True)
    fontnumber = models.TextField(blank=True, null=True)
    clicknumber = models.TextField(blank=True, null=True)
    recommandnumber = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'novel'


class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    faceimg = models.ImageField(upload_to='images')
    name = models.TextField()
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
