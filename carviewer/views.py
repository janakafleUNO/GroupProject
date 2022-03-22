from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

now = timezone.now()


# HomePage
def home(request):
    return render(request, 'carviewer/home.html',
                  {'carviewer': home})


# CarBrand
@login_required
def carbrand_list(request):
    carbrand = CarBrand.objects.filter()
    return render(request, 'carviewer/carbrand_list.html',
                  {'carbrands': carbrand})


@login_required
def carbrand_new(request):
    if request.method == "POST":
        form = CarBrandForm(request.POST)
        if form.is_valid():
            carbrand = form.save(commit=False)
            carbrand.created_date = timezone.now()
            carbrand.save()
            carbrand = CarBrand.objects.filter()
            return render(request, 'carviewer/carbrand_list.html',
                          {'carbrands': carbrand})
    else:
        form = CarTypeForm()

    return render(request, 'carviewer/cartype_new.html', {'form': form})


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


# CarType
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
            cartype = CarType.objects.filter()
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
            cartype = CarType.objects.filter()
            return render(request, 'carviewer/cartype_list.html', {'cartypes': cartype})
    else:
        form = CarTypeForm(instance=cartype)
    return render(request, 'carviewer/cartype_edit.html', {'form': form})


@login_required
def cartype_delete(request, pk):
    cartype = get_object_or_404(CarType, pk=pk)
    cartype.delete()
    return redirect('carviewer:cartype_list')


# CarModel
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
            carmodel = CarModel.objects.filter()
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
            carmodel = CarModel.objects.filter()
            return render(request, 'carviewer/carmodel_list.html', {'carmodels': carmodel})
    else:
        form = CarModelForm(instance=carmodel)
    return render(request, 'carviewer/carmodel_edit.html', {'form': form})


@login_required
def carmodel_delete(request, pk):
    carmodel = get_object_or_404(CarModel, pk=pk)
    carmodel.delete()
    return redirect('carviewer:carmodel_list')


# CarReview
@login_required
def carreview_list(request):
    carreview = CarReview.objects.filter()
    return render(request, 'carviewer/carreview_list.html',
                  {'carreviews': carreview})


@login_required
def carreview_new(request):
    if request.method == "POST":
        form = CarReviewForm(request.POST)
        if form.is_valid():
            carreview = form.save(commit=False)
            carreview.created_date = timezone.now()
            carreview.save()
            carreview = CarReview.objects.filter()
            return render(request, 'carviewer/carreview_list.html',
                          {'carreviews': carreview})
    else:
        form = CarReviewForm()

    return render(request, 'carviewer/carreview_new.html', {'form': form})


@login_required
def carreview_edit(request, pk):
    carreview = get_object_or_404(CarReview, pk=pk)
    if request.method == "POST":
        form = CarReviewForm(request.POST, instance=carreview)
        if form.is_valid():
            carreview = form.save()
            carreview.updated_date = timezone.now()
            carreview.save()
            carreview = CarReview.objects.filter()
            return render(request, 'carviewer/carreview_list.html', {'carreviews': carreview})
    else:
        form = CarReviewForm(instance=carreview)
    return render(request, 'carviewer/carreview_edit.html', {'form': form})


@login_required
def carreview_delete(request, pk):
    carreview = get_object_or_404(CarReview, pk=pk)
    carreview.delete()
    return redirect('carviewer:carreview_list')
