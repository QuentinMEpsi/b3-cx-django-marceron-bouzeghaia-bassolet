import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class Ecole(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

