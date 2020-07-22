from django.shortcuts import render
from django.http import HttpResponse

#def myView(request):
#  return HttpResponse('Home Page')

def myView(request):
  return render(request,'home.html')

