from django.shortcuts import render
from .models import TotalCandidates
import os
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'barchart/index.html')

def barplot(request):

    data_file = os.path.join('data', 'ae_contested_deposit_losts.csv')
    df = pd.read_csv(data_file)

    year = df['Year'].to_list()
    total_candidate = df['Total_Candidates'].to_list()

    context = {

        'year':year,
        'total_candidate': total_candidate
    }

    return render(request, 'barchart/barchart.html', context)