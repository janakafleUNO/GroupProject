from django.db import models
from django.utils import timezone

# Define the model for the CarViewer table


class CarBrand(models.Model):
    car_brand = models.CharField(max_length=50)
    car_year = models.IntegerField()

    def __str__(self):
        return self.car_brand


class CarType(models.Model):

    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cartypes', default=True)
    car_bodytype = models.CharField(max_length=50)
    car_fueltype = models.CharField(max_length=50)
    car_transmission = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.car_brand)


class CarModel(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='carmodels', default=True)
    model_name = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_prize = models.CharField(max_length=50)
    car_bodytype = models.CharField(max_length=50)
    car_fueltype = models.CharField(max_length=50)
    car_transmission = models.CharField(max_length=50)
    car_milage = models.CharField(max_length=50)

    def __str__(self):
        return str(self.car_brand)
