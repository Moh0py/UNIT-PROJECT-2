from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('Cars/', views.car_list, name='car_list'),        
    path('Cars/<int:car_id>/', views.car_list, name='car_list'),
    path('about/', views.about, name='about'),
    path('car_details/<int:car_id>/', views.car_details, name='car_details'),
]