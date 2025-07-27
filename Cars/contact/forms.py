from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg','placeholder': 'Enter your email address'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-lg','rows': 6,'placeholder': 'Tell us how we can help you...'}),
        }