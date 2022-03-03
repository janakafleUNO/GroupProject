from django.shortcuts import render
from .models import *
from .forms import *

def Brand(request):

    Car_Brand = Car_Brand.objects.filter()
    return render(request, 'carviewer/Brand.html',
                  {'Brands': Brand})

def Type(request):

    Car_Type = Car_Type.objects.filter()
    return render(request, 'carviewer/Type.html',
                  {'Types': Type})

def Model(request):

    Car_Model = Car_Model.objects.filter()
    return render(request, 'carviewer/Model.html',
                  {'Models': Model})

// Edit this //