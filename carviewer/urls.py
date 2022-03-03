from django.urls import path
from . import views


app_name = 'carviewer'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

path('', views.Brand, name='Brand'),
    path('Brand', views.Brand, name='Brand'),

path('', views.Name, name='Name'),
    path('Name', views.Name, name='Name'),

path('', views.Model, name='Model'),
    path('Model', views.Model, name='Model'),


// Edit This //
]