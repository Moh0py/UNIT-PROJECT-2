from django.db import models

class Car(models.Model):
    BRAND_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
    ]
    name = models.TextField(max_length=250) 
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/img/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
