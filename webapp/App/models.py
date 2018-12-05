from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    age = models.IntegerField(default=1)
    email = models.CharField(max_length=32)
    faceimg = models.ImageField(upload_to='icon')

class mainPage_img(models.Model):
    img = models.ImageField(upload_to='mainpage')

class Inovel(models.Model):
    inovel_name = models.CharField(max_length=32)
    inovel_cover = models.ImageField(upload_to='cover_img')
    inovel_type = models.CharField(max_length=12)
    inovel_author = models.CharField(default='辰东',max_length=32)