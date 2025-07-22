from django.db import models

# Create your models here.

class Car(models.Model):

    name = models.CharField(max_length=100)
    modle = models.CharField(max_length=100)
    price = models.IntegerField()
    



class Review(models.Model):
       car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
       name = models.CharField(max_length=255)
       comment = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)