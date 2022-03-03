from django.db import models
from django.utils import timezone

#Define the model for the Customer table
class Car_Brand(models.Model):
    Car_Brand = models.CharField(max_length=50, db_index=True)
    Car_Year = models.IntegerField(max_length=50, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Car_Brand'
        verbose_name_plural = 'Car_Brands'

    def __str__ (self):
        return self.Car_Brand


class Car_Type(models.Model):
    Category = models.ForeignKey(Car_Brand, related_name='products', on_delete=models.CASCADE)
    Car_BodyType = models.CharField(max_length=50)
    Car_FuelType = models.CharField(max_length=50)
    Car_Transmission = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.Car_Type


class Car_Model(models.Model):
    Model_Name = models.CharField(max_length=50)
    Car_Year = models.IntegerField(max_length=50)
    Car_Prize = models.CharField(max_length=50)
    Car_BodyType = models.CharField(max_length=50)
    Car_FuelType = models.CharField(max_length=50)
    Car_Transmission = models.CharField(max_length=50)
    Car_Milage = models.DecimalField(max_length=50)

    def __str__(self):
        return self.Car_Model