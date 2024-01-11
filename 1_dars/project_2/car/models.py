from django.db import models

# Create your models here.


class Car (models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    price = models.IntegerField()
