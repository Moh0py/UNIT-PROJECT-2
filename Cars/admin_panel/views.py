from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from main.models import Car , CarImage
from .forms import CarForm
from firebase_admin import storage

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

def upload_car_image(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        file = request.FILES.get('image')
        if file:
            bucket = storage.bucket()
            blob   = bucket.blob(f'cars/{car_id}/{file.name}')
            blob.upload_from_file(file, content_type=file.content_type)
            blob.make_public()
            url = blob.public_url

            last  = car.gallery_images.order_by('-order').first()
            order = last.order + 1 if last else 0
            CarImage.objects.create(car=car, image_url=url, order=order)

        return redirect('cars:detail', car_id=car_id)

    return render(request, 'admin_panel/upload_image.html', {'car': car})
