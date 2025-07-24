from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'), 
    path('message/', views.messages_from_users, name='messages_from_users'),  
]
