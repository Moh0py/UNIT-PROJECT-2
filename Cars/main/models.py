from django.db import models
# Create your models here.

class Car(models.Model):
    BRAND_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        
    ]
    
   

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"


class Review(models.Model):
       car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
       name = models.CharField(max_length=255)
       comment = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)