from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']

        print(uploaded_file)

        # check file type must be csv only
        if uploaded_file.name.endswith('.csv'):
            print("Upload CSV file only")
            savefile = FileSystemStorage()
            name = savefile.save(uploaded_file.name, uploaded_file)
            # where to save files

            #d = os.getcwd() # current directory of the project
            #file_directory = os.path.join(d, 'media', name)
            #print(file_directory)
        # save file in media folder
    return render(request, 'linechart/index.html')

def plot(request):
    return render(request, 'linechart/linechart.html')

def dashboard(request):
    return render(request, 'linechart/dashboard.html')