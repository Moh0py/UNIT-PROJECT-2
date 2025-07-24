from django.urls import path
from . import views
from contact import views as contact_views
from django.urls import include


urlpatterns = [
    path('', views.home_view, name='home_view'),                       
    path('about/', views.about, name='about'),                         
    path('', views.all_cars, name='all_cars'),                    
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),  
    path('search/', views.search_car, name='search_car'),             
]