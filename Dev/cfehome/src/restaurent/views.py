from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import RestaurentLocation

# Create your views here.
#function base view
#def home(request):
  #return HttpResponse("Hello")  
  #return render(request, "home.html", {}) #response


# class ContactView(View):
#   def get(self, request, *args, **kwargs):
#     print(kwargs)
#     return render(request, 'contact.html') #respose

# def home(request):
#   context = {
#     "html_var": "Test HTML TEXT from views.py",
#     "html_var2": True,
#     "some_list": ['Test', 'Test2', 'Test3', 'Test4']
#   }
#   return render(request, 'home.html', context) #respose


# def about(request):
#   return render(request, 'about.html') #respose

# class HomeTemplateView(TemplateView):
#   template_name = 'home.html'

#   def get_context_data(self, *args, **kwargs):
#     context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
#     context = {
#       "html_var": "Test HTML TEXT from views.py",
#       "html_var2": True,
#       "some_list": ['Test', 'Test2', 'Test3', 'Test4']
#     }
#     print(context)
#     return context

def restaurent_listview(request):
  template_name = 'restaurent/restaurents_list.html'
  queryset  = RestaurentLocation.objects.all()
  context = {
    "object_list": queryset
  }
  return render(request, template_name, context)