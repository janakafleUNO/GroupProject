from django.contrib import admin
from .models import Car_Type, Car_Brand


# Define the admin options for the Customer table
class Type(admin.ModelAdmin):
    list_display = ('Car_BodyType', 'Car_FuelType', 'Car_Transmission')
    list_filter = ('Car_BodyType', 'Car_FuelType')
    search_fields = ('Car_BodyType', 'Car_FuelType', 'Car_Transmission')

class Name(admin.ModelAdmin):
    list_display = ('Car_Brand', 'Car_Year')


admin.site.register(Car_Type, Type)
admin.site.register(Car_Brand, Name)
