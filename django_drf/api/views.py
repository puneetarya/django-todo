from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

def student_details(request):
    stu = Student.objects.get(id=1)
    print(f"[INFO] mode object is {stu}")

    serializer = StudentSerializer(stu)
    print(f"[INFO] python native is {serializer}")

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')