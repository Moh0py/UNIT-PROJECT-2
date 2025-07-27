
from django.urls import path, include
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about, name='about'),
    path('cars/', views.all_cars, name='all_cars'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('search/', views.search_view, name='search'),
    path('review/<int:car_id>/add/', views.add_review, name='add_review'),
    path('contact/', include('contact.urls')),
]