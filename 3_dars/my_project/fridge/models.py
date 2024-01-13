from django.db import models

# Create your models here.


class Fridge (models.Model):
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media')
    energy_custom_W = models.SmallIntegerField()



    def __str__(self):
        return self.name
