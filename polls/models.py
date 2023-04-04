import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Ecole(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank='true')
    location = models.CharField(max_length=200)
