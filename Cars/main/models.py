from django.db import models

class Car(models.Model):
    BRAND_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
    ]
    
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    description = models.TextField(blank=True, null=True)
    front_image = models.ImageField(upload_to='image/', blank=True, null=True)
    back_image  = models.ImageField(upload_to='image/', blank=True, null=True)
    model_3d_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"


class CarImage(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='gallery_images')
    image = models.ImageField(upload_to='img/gallery/')
    order = models.PositiveIntegerField(default=0,help_text="" )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image #{self.order} for {self.car}"


class Review(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='reviews')
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.car.name} by {self.name}"
