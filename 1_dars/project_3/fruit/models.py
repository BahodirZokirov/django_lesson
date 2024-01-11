from django.db import models

# Create your models here.





class Fruit (models.Model):
    name = models.CharField(max_length=25, blank=True)
    price = models.FloatField(max_length=10)
    check_price = models.DecimalField (max_digits=15, decimal_places=2)
    qayerniki = models.CharField(max_length=25, blank=True, null=True, default="Samarkand")


    def __str__(self):
        return f"{self.name}, {self.price}"