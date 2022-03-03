from django import forms
from .models import Car_Brand, Car_Type, Car_Model

class Car_Brand(forms.ModelForm):
    class Meta:
        model = Car_Brand
        fields = ( 'Car_Brand', 'image' )

class Car_Type(forms.ModelForm):
    class Meta:
        model = Car_Type
        fields = ( 'Category', 'Car_BodyType', 'Car_FuelType', 'Car_Transmission', 'description', 'available' )

class Car_Model(forms.ModelForm):
    class Meta:
        model = Car_Model
        fields = ( 'Model_Name', 'Car_Year', 'Car_Prize', 'Car_BodyType', 'Car_FuelType', 'Car_Transmission', 'Car_Milage' )

//Edit this//