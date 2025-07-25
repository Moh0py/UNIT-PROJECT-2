from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import ContactMessage

def about(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messages_from_users')
    else:
        form = ContactMessageForm()

    return render(request, 'contact/about.html', {'form': form})


def messages_from_users(request):
    messages = ContactMessage.objects.all()
    return render(request, 'contact/contact_message.html', {'messages': messages})
