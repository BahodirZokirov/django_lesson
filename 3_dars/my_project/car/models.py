from django.db import models

# Create your models here.



class Car (models.Model):
    name = models.CharField(max_length=25)
    make = models.CharField(max_length=25)
    image = models.ImageField(upload_to='media')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    motor_type = models.CharField(max_length=20)




    def __str__(self):
        return self.name
