from django.shortcuts import render, redirect, get_object_or_404
from main.models import Car, CarImage
from .forms import CarForm

def admin_cars(request):
    cars = Car.objects.all()
    return render(request, 'admin_panel/admin_cars.html', {'cars': cars})

def details_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'admin_panel/details_car.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        print("POST data:", request.POST)  
        print("FILES data:", request.FILES)  
        
        if form.is_valid():
            car = form.save()
            print(f"Car saved: {car.id}") 
            
            back_images = request.FILES.getlist('back_images')
            print(f"Back images count: {len(back_images)}")  
            
            for index, image in enumerate(back_images):
                car_image = CarImage.objects.create(
                    car=car,
                    image=image,
                    order=index
                )
                print(f"Image saved: {car_image.id}")  
            
            return redirect('admin_panel:admin_cars')
        else:
            print("Form errors:", form.errors)
            print("Form is invalid")
    else:
        form = CarForm()
    
    return render(request, 'admin_panel/add_car.html', {'form': form})
def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:admin_cars')
    else:
        form = CarForm(instance=car)
    return render(request, 'admin_panel/update_car.html', {'form': form, 'car': car})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('admin_panel:admin_cars')
    return render(request, 'admin_panel/delete_car.html', {'car': car})

def upload_car_image(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        
        
        last = car.gallery_images.order_by('-order').first()
        order = last.order + 1 if last else 0
        
        for f in files:
            CarImage.objects.create(
                car=car,
                image=f,  
                order=order
            )
            order += 1
        
        return redirect('admin_panel:details_car', car_id=car.id)  
    
    return render(request, 'admin_panel/upload_images.html', {'car': car})