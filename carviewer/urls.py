from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'carviewer'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('carbrand_list', views.carbrand_list, name='carbrand_list'),
    path('carbrand/create/', views.carbrand_new, name='carbrand_new'),
    path('carbrand/<int:pk>/edit/', views.carbrand_edit, name='carbrand_edit'),
    path('carbrand/<int:pk>/delete/', views.carbrand_delete, name='carbrand_delete'),
    path('cartype_list', views.cartype_list, name='cartype_list'),
    path('cartype/create/', views.cartype_new, name='cartype_new'),
    path('cartype/<int:pk>/edit/', views.cartype_edit, name='cartype_edit'),
    path('cartype/<int:pk>/delete/', views.cartype_delete, name='cartype_delete'),
    path('carmodel_list', views.carmodel_list, name='carmodel_list'),
    path('carmodel/create/', views.carmodel_new, name='carmodel_new'),
    path('carmodel/<int:pk>/edit/', views.carmodel_edit, name='carmodel_edit'),
    path('carmodel/<int:pk>/delete/', views.carmodel_delete, name='carmodel_delete'),
    path('carreview_list', views.carreview_list, name='carreview_list'),
    path('carreview/create/', views.carreview_new, name='carreview_new'),
    path('carreview/<int:pk>/edit/', views.carreview_edit, name='carreview_edit'),
    path('carreview/<int:pk>/delete/', views.carreview_delete, name='carreview_delete'),
]
