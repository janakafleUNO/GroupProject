from django.db import models
from django.utils import timezone

#Define the model for the Customer table
class Car_Brand(models.Model):
    Car_Brand = models.CharField(max_length=50)
    Car_Year = models.CharField(max_length=50)

    def __str__ (self):
        return self.Car_Brand
class Car_Type(models.Model):
    Car_BodyType = models.CharField(max_length=50)
    Car_FuelType = models.CharField(max_length=50)
    Car_Transmission = models.CharField(max_length=50)

    def __str__(self):
        return self.Car_Type