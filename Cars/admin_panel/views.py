from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from main.models import Car
from .forms import CarForm

def is_staff(user):
    return user.is_staff


def admin_cars(request):
    cars = Car.objects.all()
    return render(request, 'admin_panel/admin_cars.html', {'cars': cars})


def details_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'admin_panel/details_car.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_cars') 
    else:
        form = CarForm()
    return render(request, 'admin_panel/add_car.html', {'form': form})


def update_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('admin_cars')
    else:
        form = CarForm(instance=car)
    return render(request, 'admin_panel/update_car.html', {'form': form, 'car': car})


def delete_car(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        car.delete()
        return redirect('admin_cars')
    return render(request, 'admin_panel/delete_car.html', {'car': car})
