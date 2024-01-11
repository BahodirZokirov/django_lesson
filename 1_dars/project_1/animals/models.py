from django.db import models

# Create your models here.

class Animal (models.Model):
    name = models.CharField(max_length=25)
    kind = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    max_size = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name




class Students (models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name