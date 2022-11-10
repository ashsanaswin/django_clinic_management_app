from django import forms
from . import models
from .models import Appoinment

class AppoForm(forms.ModelForm):
  class Meta:
    model = Appoinment
    fields = ['first_name','last_name','email','phone_number','date','time','department']

