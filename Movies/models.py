from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
AGE_CHOICES=(
    ('All','All'),
    ('kids','kids')
)
MOVIE_CHOICE=(
    ('seasonal','Seasonal'),
    ('single','Single')
)

class customUser(AbstractUser):
    profiles=models.ManyToManyField('profiles',null=True,blank=True)

class profile(models.Model):
    name=models.CharField(max_length=300)
    age_limit=models.CharField(max_length=20,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

class movies(models.Model):
    title=models.CharField(max_length=60)
    description=models.CharField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=30,choices=MOVIE_CHOICE)
    video=models.ManyToManyField('video')
    media=models.ImageField(upload_to='media')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)

class Video(models.Model):
    title=models.CharField(max_length=30,blank=True, null=True)
    file=models.FileField(upload_to='movies')

