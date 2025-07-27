from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import ContactMessage

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('messages_from_users')
    
    return render(request, 'contact/about.html')

def messages_from_users(request):
    messages = ContactMessage.objects.all()
    return render(request, 'contact/contact_message.html', {'messages': messages})