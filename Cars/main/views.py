from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Car, Review
from .forms import CarForm, ReviewForm, CarFilterForm

def home_view(request):
    cars = Car.objects.all()[:3]  
    return render(request, 'pages/home.html', {'cars': cars})

def all_cars(request):
    cars = Car.objects.all()

    brand = request.GET.get('brand')
    if brand:
        cars = cars.filter(brand=brand)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)

    paginator = Paginator(cars, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/all_cars.html', {'page_obj': page_obj})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)  
    related_cars = Car.objects.filter(brand=car.brand).exclude(pk=car_id)[:4]
    reviews = car.reviews.all()

    context = {
        'car': car,
        'related_cars': related_cars,
        'reviews': reviews,
        'form': ReviewForm()
    }
    return render(request, 'pages/car_detail.html', context)


def about(request):
    return render(request, 'contact/about.html')

def contact(request):
    return render(request, 'contact/contact.html')

def search_car(request):
    query = request.GET.get('q', '')
    if query:
        results = Car.objects.filter(name__icontains=query)
    else:
        results = Car.objects.all()

    return render(request, 'cars/search.html', {'results': results, 'query': query})


def add_review(request, car_id):

 if request.method == 'POST':
      car = Car.objects.get(pk=car_id)
      review_text = Review(car=car, name=request.POST.get('name'), comment=request.POST.get('comment'))
      review_text.save()
      return redirect('car_detail', car_id=car.id)

