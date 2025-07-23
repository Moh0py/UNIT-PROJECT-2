from django import forms
from main.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price',  'description', 'image']
