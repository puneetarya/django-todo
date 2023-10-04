from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("puneet", views.puneet, name="puneet"),
    path("<str:name>", views.greet, name="greet")
]
