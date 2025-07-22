from django.shortcuts import render
from .models import Car

# Create your views here.


def home(request):
    return render(request,'pages/home.html')




def home(request):
    cars = Car.objects.all()
    return render(request, 'pages/home.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.all(Car, pk=car_id)
    return render(request, 'pages/car.html', {'car': car})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
