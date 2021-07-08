from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
CHO

class customUser(AbstractUser):
    profiles=models.ManyToManyField('profiles',null=True,blank=True)

class profile=(models.Model):
    name=models.CharField(max_length=300)
    age_limit=models.CharField(max_length=20,choices=c)