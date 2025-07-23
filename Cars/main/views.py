from django.shortcuts import render , redirect
from .models import Car
from django.conf import settings

# Create your views here.
def home_view(request):
    cars = Car.objects.all()
    return render(request, 'pages/home.html', {'cars': cars})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'pages/car_list.html', {'cars': cars})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'contact/contact.html')

def car_details(request,car_id):
    car = Car.objects.all(Car, pk=car_id)
    return render(request,'pages/deatils.html',{'car':car})