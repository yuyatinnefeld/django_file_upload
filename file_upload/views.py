from django.shortcuts import render
from django.http import HttpResponseRedirect

def fileUploadView(request):
    return render(request, 'file_upload.html')

def fileUploadRun(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['filename']
        print(uploaded_file.name)
        print(uploaded_file.size)

    return render(request,'file_upload_result.html')    
    