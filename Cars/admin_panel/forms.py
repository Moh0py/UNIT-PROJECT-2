from django import forms
from main.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price', 'brand', 'description', 'front_image', 'back_image', 'model_3d_url']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'brand': forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'front_image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'back_image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'model_3d_url': forms.URLInput(attrs={'class':'form-control'}),
        }
