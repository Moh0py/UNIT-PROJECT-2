from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from .models import ContactMessage

def contact_us(request):  # تغيير اسم الدالة ليطابق urls.py
    print(f"Request method: {request.method}")
    
    if request.method == 'POST':
        print("POST request received")
        print(f"POST data: {request.POST}")
        
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        print(f"Name: '{name}', Email: '{email}', Message: '{message}'")
        
        if name and email and message:
            print("All fields are filled - attempting to save")
            try:
                contact_msg = ContactMessage.objects.create(
                    name=name,
                    email=email,
                    message=message
                )
                print(f"Message saved successfully with ID: {contact_msg.id}")
                
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
                print("Redirecting to messages_from_users")
                return redirect('messages_from_users')
                
            except Exception as e:
                print(f"Error saving message: {str(e)}")
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
        else:
            print("Missing required fields:")
            print(f"Name empty: {not name}, Email empty: {not email}, Message empty: {not message}")
            messages.error(request, 'Please fill in all required fields.')
    
    form = ContactMessageForm()
    print("Rendering contact.html template")
    return render(request, 'contact/contact.html', {'form': form})  # تصحيح: contact.html وليس contact_messages.html

def messages_from_users(request):
    print("messages_from_users view called")
    contact_messages = ContactMessage.objects.all().order_by('-created_at')  # تصحيح: ContactMessage بدلاً من Contactmessage
    print(f"Found {contact_messages.count()} messages in database")
    
    context = {
        'messages': contact_messages,
        'total_messages': contact_messages.count(),
    }
    
    return render(request, 'contact/contact_messages.html', context)