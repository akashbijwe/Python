from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#function base view
#def home(request):
  #return HttpResponse("Hello")  
  #return render(request, "home.html", {}) #response

def home(request):
  context = {
    "html_var": "Test HTML TEXT from views.py",
    "html_var2": True,
    "some_list": ['Test', 'Test2', 'Test3', 'Test4']
  }
  return render(request, 'home.html', context) #respose


def about(request):
  return render(request, 'about.html') #respose


def contact(request):
  return render(request, 'contact.html') #respose