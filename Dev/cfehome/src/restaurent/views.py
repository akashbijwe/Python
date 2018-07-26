from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurentLocation
from .forms import RestaurentCreateForm

# Create your views here.
#function base view
#def home(request):
  #return HttpResponse("Hello")  
  #return render(request, "home.html", {}) #response


# class ContactView(View):
#   def get(self, request, *args, **kwargs):
#     print(kwargs)
#     return render(request, 'contact.html') #respose

def home(request):
  context = {
    "html_var": "Test HTML TEXT from views.py",
    "html_var2": True,
    "some_list": ['Test', 'Test2', 'Test3', 'Test4']
  }
  return render(request, 'home.html', context) #respose


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

#Template View
def RestaurentListView(request):
  template_name = 'restaurent/restaurents_list.html'
  queryset  = RestaurentLocation.objects.all()
  context = {
    "object_list": queryset
  }
  return render(request, template_name, context)


#List View
# class RestaurentListView(ListView):
#   queryset = RestaurentLocation.objects.all()
#   template_name = 'restaurent/restaurents_list.html'
  
  
# class NonVegRestaurentListView(ListView):
#   queryset = RestaurentLocation.objects.filter(category__iexact='non-veg')
#   template_name = 'restaurent/restaurents_list.html'

# class VegRestaurentListView(ListView):
#   queryset = RestaurentLocation.objects.filter(category__iexact='veg')
#   template_name = 'restaurent/restaurents_list.html'

# class SearchRestaurentListView(ListView):
#   template_name = 'restaurent/restaurents_list.html'
#   def get_queryset(self):
#     print(self.kwargs)
#     slug = self.kwargs.get("slug")
#     if slug:
#       queryset = RestaurentLocation.objects.filter(category__iexact=slug)
#     else:
#       queryset = RestaurentLocation.objects.all()
#     return queryset

def RestaurentDetailView(request, slug):
  obj = RestaurentLocation.objects.get(slug=slug)
  template_name = 'restaurent/restaurentlocation_detail.html'
  context = {
    "object": obj
  }
  return render(request, template_name, context)

def RestaurentCreateForm(request):
  template_name = 'restaurent/restaurectlocation_create.html'
  context = {}
  print(request.POST)
  return render(request, template_name, context)

  # def get_context_data(self, *args, **kwargs):
  #   print(self.kwargs)
  #   context = super(RestaurentDetailView, self).get_context_data(*args, **kwargs)
  #   print(context)
  #   return context

  # def get_object(self, *args, **kwargs):
  #   rest_id = self.kwargs.get('rest_id')
  #   obj = get_object_or_404(RestaurentLocation, id=rest_id)
  #   return obj


