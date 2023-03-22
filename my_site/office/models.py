from operator import mod
from pyexpat import model
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()