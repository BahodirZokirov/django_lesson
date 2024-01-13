from django.db import models

# Create your models here.


class TV (models.Model):
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    price = models.SmallIntegerField()
    screen_size = models.PositiveSmallIntegerField()
    custom_energy_W = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.name
