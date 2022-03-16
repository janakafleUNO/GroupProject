
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
now = timezone.now()


def home(request):
    return render(request, 'carviewer/home.html',
                  {'carviewer': home})


@login_required
def carbrand_list(request):
    carbrand = CarBrand.objects.filter()
    return render(request, 'carviewer/carbrand_list.html',
                  {'carbrands': carbrand})


@login_required
def carbrand_edit(request, pk):
    carbrand = get_object_or_404(CarBrand, pk=pk)
    if request.method == "POST":
        # update
        form = CarBrandForm(request.POST, instance=carbrand)
        if form.is_valid():
            carbrand = form.save(commit=False)
            carbrand.updated_date = timezone.now()
            carbrand.save()
            carbrand = CarBrand.objects.filter()
            return render(request, 'carviewer/carbrand_list.html',
                          {'carbrands': carbrand})
    else:
        # edit
        form = CarBrandForm(instance=carbrand)
    return render(request, 'carviewer/carbrand_edit.html', {'form': form})


@login_required
def carbrand_delete(request, pk):
    carbrand = get_object_or_404(CarBrand, pk=pk)
    carbrand.delete()
    return redirect('carviewer:carbrand_list')


@login_required
def cartype_list(request):
    cartype = CarType.objects.filter()
    return render(request, 'carviewer/cartype_list.html',
                  {'cartypes': cartype})


@login_required
def cartype_new(request):
    if request.method == "POST":
        form = CarTypeForm(request.POST)
        if form.is_valid():
            cartype = form.save(commit=False)
            cartype.created_date = timezone.now()
            cartype.save()
            cartype = CarType.objects.filter(created_date__lte=timezone.now())
            return render(request, 'carviewer/cartype_list.html',
                          {'cartypes': cartype})
    else:
        form = CarTypeForm()

    return render(request, 'carviewer/cartype_new.html', {'form': form})


@login_required
def cartype_edit(request, pk):
    cartype = get_object_or_404(CarType, pk=pk)
    if request.method == "POST":
        form = CarTypeForm(request.POST, instance=cartype)
        if form.is_valid():
            cartype = form.save()
            cartype.updated_date = timezone.now()
            cartype.save()
            cartype = CarType.objects.filter(created_date__lte=timezone.now())
            return render(request, 'carviewer/cartype_list.html', {'cartypes': cartype})
    else:
        form = CarTypeForm(instance=cartype)
    return render(request, 'carviewer/cartype_edit.html', {'form': form})


@login_required
def cartype_delete(request, pk):
    cartype = get_object_or_404(CarType, pk=pk)
    cartype.delete()
    return redirect('carviewer:cartype_list')



@login_required
def carmodel_list(request):
    carmodel = CarModel.objects.filter()
    return render(request, 'carviewer/carmodel_list.html',
                  {'carmodels': carmodel})


@login_required
def carmodel_new(request):
    if request.method == "POST":
        form = CarModelForm(request.POST)
        if form.is_valid():
            carmodel = form.save(commit=False)
            carmodel.created_date = timezone.now()
            carmodel.save()
            carmodel = CarModel.objects.filter(created_date__lte=timezone.now())
            return render(request, 'carviewer/carmodel_list.html',
                          {'carmodels': carmodel})
    else:
        form = CarModelForm()

    return render(request, 'carviewer/carmodel_new.html', {'form': form})


@login_required
def carmodel_edit(request, pk):
    carmodel = get_object_or_404(CarModel, pk=pk)
    if request.method == "POST":
        form = CarModelForm(request.POST, instance=carmodel)
        if form.is_valid():
            carmodel = form.save()
            carmodel.updated_date = timezone.now()
            carmodel.save()
            carmodel = CarModel.objects.filter(created_date__lte=timezone.now())
            return render(request, 'carviewer/carmodel_list.html', {'carmodels': carmodel})
    else:
        form = CarModelForm(instance=carmodel)
    return render(request, 'carviewer/carmodel_edit.html', {'form': form})


@login_required
def carmodel_delete(request, pk):
    carmodel = get_object_or_404(CarModel, pk=pk)
    carmodel.delete()
    return redirect('carviewer:carmodel_list')




