from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages
import pandas as pd
# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']

        print(uploaded_file)

        # check file type must be csv only
        if uploaded_file.name.endswith('.csv'):
            print("Upload CSV file")
            savefile = FileSystemStorage()
            name = savefile.save(uploaded_file.name, uploaded_file)
            # where to save files
            # save file in media folder
            d = os.getcwd() # current directory of the project
            file_directory = os.path.join(d, 'media', name)
            print(file_directory)
            readfile(file_directory)
            
            return redirect(dashboard)
        else:
            messages.warning(request, 'File was not uploaded. Please upload CSV file only')
        
    return render(request, 'linechart/index.html')

def lineplot(request):

    data_file = os.path.join('data','turnout_karnataka.csv')
    df = pd.read_csv(data_file)

    year = df['Year'].to_list()
    turnout = df['total'].to_list()

    context = {
        'year':year,
        'turnout':turnout
    }
    return render(request, 'linechart/linechart.html', context)

def dashboard(request):
    message = f"[INFO] The uploaded dataset file has {cnt_rows} Rows"

    messages.warning(request,message)

    return render(request, 'linechart/dashboard.html')

def readfile(filename):

    my_file = pd.read_csv(filename)

    global cnt_rows, cnt_cols, cols_name, cols_dtype, data_top5, f_name, missing_report

    cnt_rows = len(my_file)
    cnt_cols = len(my_file.columns)
    cols_name = list(my_file.columns)
    cols_dtype = list(my_file.dtypes)
    data_top5 = my_file[:5]
    f_name = filename
    missing_report = my_file.isna().sum()

    '''
    print({'Rows':cnt_rows,
           'Cols':cnt_cols,
           'Column Name':cols_name,
           'Column Data Type':cols_dtype,
           'Data_Top5': data_top5,
           'Filename':f_name,
           'Missing_Values':missing_report})
    '''