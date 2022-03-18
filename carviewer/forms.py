from django import forms
from .models import CarBrand, CarType, CarModel


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ('car_brand', 'car_year')


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = ('car_brand', 'car_bodytype', 'car_fueltype', 'car_transmission', 'description', 'available')


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('car_brand', 'model_name', 'car_year', 'car_price', 'car_bodytype', 'car_fueltype', 'car_transmission',
                  'car_mileage')
