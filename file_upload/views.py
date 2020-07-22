from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pandas as pd

def fileUploadView(request):
    return render(request, 'file_upload.html')

def fileUploadRun(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['filename'] 
        uploaded_filename = uploaded_file.name
        #save the uploaded file in the media forder
        fs = FileSystemStorage()
        fs.save(uploaded_filename, uploaded_file)

        ###HIER DU MUSS WAS MACHEN!!!!!
        csv = f"./media/{uploaded_filename}"
        df = pd.read_csv(csv)
        print(df(2))

    return render(request,'file_upload_result.html')    
    