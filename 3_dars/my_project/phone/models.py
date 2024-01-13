from django.db import models

# Create your models here.


class Phone (models.Model):
    name = models.CharField(max_length=22)
    make = models.CharField(max_length=22)
    color = models.CharField(max_length=22)
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # CPU = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name


