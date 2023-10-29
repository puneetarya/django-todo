from django.shortcuts import render
from .models import TotalCandidates

# Create your views here.
def index(request):
    return render(request, 'barchart/index.html')

def plot(request):

    data = TotalCandidates.objects.all()
    context = {
        'data':data
    }

    return render(request, 'barchart/barchart.html', context)