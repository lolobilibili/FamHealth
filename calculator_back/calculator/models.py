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
  username = models.CharField(max_length=100,primary_key=True)
  password = models.CharField(max_length=500)

class User_group(models.Model):
  username = models.CharField(max_length=100,primary_key=True)
  group_id = models.IntegerField(default= 0)
  text  = models.TextField(default="")

class Score_record(models.Model):
  username = models.CharField(max_length=100,primary_key=True)
  bmi = models.FloatField(default=0)
  vital_capacity = models.IntegerField(default=0)
  run_50 = models.FloatField(default=0)
  sit_and_reach = models.FloatField(default=0)
  jump = models.FloatField(default=0)
  Pull_ups_and_sit_ups = models.IntegerField(default=0)
  run_1000 = models.FloatField(default=0)
  run_1000_performance=models.CharField(max_length=100,default='')

  bmi_score=models.IntegerField(default=0)
  vital_capacity_score=models.IntegerField(default=0)
  run_50_score=models.IntegerField(default=0)
  sit_and_reach_score=models.IntegerField(default=0)
  jump_score=models.IntegerField(default=0)
  Pull_ups_and_sit_ups_score=models.IntegerField(default=0)
  run_1000_score=models.IntegerField(default=0)
  score=models.FloatField(default=0)
  suggestion=models.CharField(max_length=200,default='')