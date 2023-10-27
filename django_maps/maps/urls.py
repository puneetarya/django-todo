from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("karnataka", views.karnataka, name="karnataka"),
    path("world", views.world, name="world"),
    path("india", views.india, name="india"),
   
]
