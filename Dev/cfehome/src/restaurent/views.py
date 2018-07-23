from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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

class ContactView(View):
  def get(self, request, *args, **kwargs):
    print(kwargs)
    return render(request, 'contact.html') #respose