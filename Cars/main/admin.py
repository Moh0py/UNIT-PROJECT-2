from django.contrib import admin
from .models import Car, CarImage

# Register your models here.

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 3 
    fields = ('order', 'image')


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'brand')
    inlines = [CarImageInline]
