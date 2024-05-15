#models.py
from django.db import models
import os
# Create your models here.
class breakfast(models.Model):
  date = models.DateField(primary_key=True)
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)

class lunch(models.Model):
  date = models.DateField(primary_key=True)
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)

class dinner(models.Model):
  date = models.DateField(primary_key=True)
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)

class snack(models.Model):
  date = models.DateField(primary_key=True)
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)

class sport(models.Model):
  date = models.DateField(primary_key=True)
  hot = models.IntegerField(default = 0)
  des = models.CharField(max_length=1000)