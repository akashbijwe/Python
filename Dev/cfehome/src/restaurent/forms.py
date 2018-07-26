from django import forms

class RestaurentCreateForm(forms.Form):
  name      = forms.CharField()
  location  = forms.CharField(required=False)
  category  = forms.CharField(required=False)