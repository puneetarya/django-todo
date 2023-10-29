from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'linechart/index.html')

def plot(request):
    return render(request, 'linechart/linechart.html')