from django.contrib import admin

# Register your models here.


from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']