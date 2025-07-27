from django.urls import path
from . import views


app_name='admin_panel'

urlpatterns = [
    path('cars/', views.admin_cars, name='admin_cars'),
    path('cars/add/', views.add_car, name='add_car'),
    path('cars/<int:car_id>/', views.details_car, name='details_car'),
    path('cars/update/<int:car_id>/', views.update_car, name='update_car'),
    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),
    path('cars/<int:car_id>/upload/', views.upload_car_image, name='upload_image'),
]
