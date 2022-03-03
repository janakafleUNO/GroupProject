from django.contrib import admin
from .models import Car_Type, Car_Brand, Car_Model


# Define the admin options for the Customer table

class Brand(admin.ModelAdmin):
    list_display = ('Car_Brand', 'Car_Year')
    list_filter = ('Car_Brand', 'Car_Year')

class Type(admin.ModelAdmin):
    list_display = ('Car_BodyType', 'Car_FuelType', 'Car_Transmission', 'available',)
    list_filter = ('Car_BodyType', 'Car_FuelType')
    search_fields = ('Car_BodyType', 'Car_FuelType', 'Car_Transmission')
    list_editable = ('Car_BodyType', 'Car_FuelType', 'Car_Transmission', 'available',)

class Model(admin.ModelAdmin):
    list_display = ('Model_Name', 'Car_Year', 'Car_Prize', 'Car_BodyType', 'Car_FuelType', 'Car_Transmission', 'Car_Milage')
    list_filter = ('Model_Name', 'Car_Year', 'Car_Prize', 'Car_BodyType', 'Car_FuelType', 'Car_Transmission')
    search_fields = ('Model_Name', 'Car_Year')


admin.site.register(Car_Brand, Brand)
admin.site.register(Car_Type, Type)
admin.site.register(Car_Model, Model)
