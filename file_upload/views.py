from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pandas as pd

def fileUploadView(request):
    return render(request, 'file_upload.html')

def fileUploadRun(request):

    info = {}

    if request.method == 'POST':
        uploaded_file = request.FILES['filename'] 
        uploaded_filename = uploaded_file.name
        
        #save the uploaded file in the media forder
        fs = FileSystemStorage()
        fs.save(uploaded_filename, uploaded_file)
        csv_file = f"./media/{uploaded_filename}"
        df = pd.read_csv(csv_file) # print(df)
        url_list = []
      
        for url in df['URL'].unique():
          #print(url)
          url_list.append(url)
               

    info['URL'] = url_list
    info['Category'] = {'brand','ecommerce','finace','ecommerce'}

    return render(request,'file_upload_result.html',{'info':info})
    