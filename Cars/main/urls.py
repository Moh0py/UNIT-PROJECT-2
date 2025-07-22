from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('Cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('about/', views.about, name='about'),
]
