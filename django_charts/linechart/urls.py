from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("plot", views.plot, name="linechart"),
    path("dashboard", views.dashboard, name="dashboard")
]
