from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.admin_cars, name='admin_cars'),
    path('cars/add/', views.add_car, name='add_car'),
    path('cars/update/<int:pk>/', views.update_car, name='update_car'),
    path('cars/delete/<int:pk>/', views.delete_car, name='delete_car'),
   
]
