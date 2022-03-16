from django.contrib import admin
from .models import CarType, CarBrand, CarModel


class CarBrandList(admin.ModelAdmin):
    list_display = ('car_brand', 'car_year')
    list_filter = ('car_brand', 'car_year')
    ordering = ['car_brand']


class CarTypeList(admin.ModelAdmin):
    list_display = ('car_brand', 'car_bodytype', 'car_fueltype', 'car_transmission')
    list_filter = ('car_brand', 'car_bodytype', 'car_fueltype')
    search_fields = ('car_brand', 'car_bodytype', 'car_fueltype', 'car_transmission')
    ordering = ['car_brand']


class CarModelList(admin.ModelAdmin):
    list_display = (
        'car_brand',  'model_name', 'car_year', 'car_prize', 'car_bodytype', 'car_fueltype', 'car_transmission',
        'car_milage')
    list_filter = (
        'car_brand', 'model_name', 'car_year', 'car_prize', 'car_bodytype', 'car_fueltype', 'car_transmission')
    search_fields = ('car_brand', 'model_name', 'car_year')
    ordering = ['car_brand']


admin.site.register(CarBrand, CarBrandList)
admin.site.register(CarType, CarTypeList)
admin.site.register(CarModel, CarModelList)
