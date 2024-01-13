from django.db import models

# Create your models here.


class Laptop (models.Model):
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    CPU = models.PositiveSmallIntegerField()
    memory = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media')




    def __str__(self):
        return self.name
