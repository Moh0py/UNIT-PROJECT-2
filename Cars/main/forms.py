from django import forms
from .models import Car, Review

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'price', 'brand', 'image']

        widgets = {
            'year': forms.NumberInput(attrs={'min': 1900, 'max': 2100}),
            'price': forms.NumberInput(attrs={'step': 0.01}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'comment']

        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
        }

class CarFilterForm(forms.Form):
    brand = forms.ChoiceField(
        choices=[('', 'All Brands'), 
                 ('Toyota', 'Toyota'), 
                 ('Ford', 'Ford'), 
                 ('BMW', 'BMW'), 
                 ('Mercedes', 'Mercedes')],
        required=False,
        label='Brand'
    )
    min_price = forms.DecimalField(
        required=False, 
        min_value=0, 
        widget=forms.NumberInput(attrs={'placeholder': 'Min Price'}), 
        label='Min Price'
    )
    max_price = forms.DecimalField(
        required=False, 
        min_value=0, 
        widget=forms.NumberInput(attrs={'placeholder': 'Max Price'}), 
        label='Max Price'
    )
