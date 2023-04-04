import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Ecole(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

