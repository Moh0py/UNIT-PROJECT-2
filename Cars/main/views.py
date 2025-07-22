from django.shortcuts import render , redirect
from .models import Car
from django.conf import settings
import smartcar

# Create your views here.
def home_view(request):
    cars = Car.objects.all()
    return render(request, 'pages/home.html', {'cars': cars})





def smartcar_connect(request):
    client = smartcar.AuthClient(
        client_id=settings.SMARTCAR_CLIENT_ID,
        client_secret=settings.SMARTCAR_CLIENT_SECRET,
        redirect_uri=settings.SMARTCAR_REDIRECT_URI,
    )
    auth_url = client.get_auth_url()
    return redirect(auth_url)


def smartcar_callback(request):
    code = request.GET.get('code')
    client = smartcar.AuthClient(
        client_id=settings.SMARTCAR_CLIENT_ID,
        client_secret=settings.SMARTCAR_CLIENT_SECRET,
        redirect_uri=settings.SMARTCAR_REDIRECT_URI,
        scope=settings.SMARTCAR_SCOPES,
        test_mode=True
    )
    access = client.exchange_code(code)
    access_token = access['access_token']

    response = smartcar.get_vehicles(access_token)
    vehicles = response['vehicles']  

    cars_data = []
    for vehicle_id in vehicles:
        vehicle = smartcar.Vehicle(vehicle_id, access_token)
        info = vehicle.info()
        odometer = vehicle.odometer()
        cars_data.append({
            "info": info,
            "odometer": odometer,
        })

    return render(request, 'pages/smartcar_list.html', {'cars': cars_data})




def car_detail(request, car_id):
    car = Car.objects.all(Car, pk=car_id)
    return render(request, 'pages/car.html', {'car': car})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'contact/contact.html')
