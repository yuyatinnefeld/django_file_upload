from django.shortcuts import render
from django.http import HttpResponse

#def myView(request):
#  return HttpResponse('Home Page')

def myView(request):
  return render(request,'home.html')


def getformView(request):
  return render(request,'test_getform.html')


def postformView(request):
  return render(request,'test_postform.html')


def fileuploadView(request):
  return render(request,'file_upload.html')