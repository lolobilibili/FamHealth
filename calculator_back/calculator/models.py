#models.py
from django.db import models
import os
# Create your models here.
class breakfast(models.Model):
  
  date = models.DateField()
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)
  username = models.CharField(max_length=100)
  class Meta:
    unique_together = ("date", "username")

class lunch(models.Model):
  
  date = models.DateField()
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)
  username = models.CharField(max_length=100)
  class Meta:
    unique_together = ("date", "username")

class dinner(models.Model):
  
  date = models.DateField()
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)
  username = models.CharField(max_length=100)
  class Meta:
    unique_together = ("date", "username")
class snack(models.Model):
  
  date = models.DateField()
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)
  username = models.CharField(max_length=100)
  class Meta:
    unique_together = ("date", "username")
class sport(models.Model):
  
  date = models.DateField()
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)
  username = models.CharField(max_length=100)
  class Meta:
    unique_together = ("date", "username")

class User(models.Model):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=500)

class User_group(models.Model):
  username = models.CharField(max_length=100)
  group_id = models.IntegerField(default= 0)
  text  = models.TextField(default="")