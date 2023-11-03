from django.urls import path
from api import views

urlpatterns = [
    path("student_details", views.student_details, name='student_details')
]
