from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test
from main.models import Car, CarImage
from .forms import CarForm
from firebase_admin import storage

def is_staff(user):
    return user.is_staff

def admin_cars(request):
    cars = Car.objects.all()
    return render(request, 'admin_panel/admin_cars.html', {'cars': cars})

def details_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404("Car not found")
    return render(request, 'admin_panel/details_car.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:admin_cars')
    else:
        form = CarForm()
    return render(request, 'admin_panel/add_car.html', {'form': form})

def update_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404("Car not found")
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:admin_cars')
    else:
        form = CarForm(instance=car)
    return render(request, 'admin_panel/update_car.html', {'form': form, 'car': car})

def delete_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404("Car not found")
    if request.method == 'POST':
        car.delete()
        return redirect('admin_panel:admin_cars')
    return render(request, 'admin_panel/delete_car.html', {'car': car})

def upload_car_image(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'POST':
        files = request.FILES.getlist('images')
        bucket = storage.bucket()
        last = car.gallery_images.order_by('-order').first()
        order = last.order + 1 if last else 0

        for f in files:
            blob = bucket.blob(f'cars/{car.id}/{f.name}')
            blob.upload_from_file(f, content_type=f.content_type)
            blob.make_public()
            CarImage.objects.create(
                car=car,
                image_url=blob.public_url,
                order=order
            )
            order += 1

        return redirect('admin_panel:detail', car_id=car.id)