from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models



class DoctorUserForm(forms.ModelForm):
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  username = forms.CharField(required=True)
  password1= forms.CharField(required=True)
  password2= forms.CharField(required=True)
  class Meta:
    model = User
    fields = ['first_name','last_name','email','username','password1','password2']

class DoctorForm(forms.ModelForm):
  class Meta:
    model = models.Doctor
    fields = ['phone_number','specialization','medical_degrees','department']



class NewUserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  username = forms.CharField(required=True)
  password1= forms.CharField(required=True)
  password2= forms.CharField(required=True)
  


  class Meta:
    model = User
    fields = ('email','username','password1','password2')
  
  def save(self, commit = True): 
      user = super(NewUserForm, self).save(commit=False)
      user.email = self.cleaned_data['email']
      if commit:
        user.save()
      
      return user



class ReceptionUserForm(forms.ModelForm):
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  username = forms.CharField(required=True)
  password1= forms.CharField(required=True)
  password2= forms.CharField(required=True)
  class Meta:
    model = User
    fields = ['first_name','last_name','email','username','password1','password2']
  
  def save(self, commit = True): 
      user = super(ReceptionUserForm, self).save(commit=False)
      user.email = self.cleaned_data['email']
      if commit:
        user.save()
      
      return user



class PharmacyUserForm(forms.ModelForm):
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  username = forms.CharField(required=True)
  password1= forms.CharField(required=True)
  password2= forms.CharField(required=True)
  class Meta:
    model = User
    fields = ['first_name','last_name','email','username','password1','password2']
  
  def save(self, commit = True): 
      user = super(PharmacyUserForm, self).save(commit=False)
      user.email = self.cleaned_data['email']
      if commit:
        user.save()
      
      return user



class NurseUserForm(forms.ModelForm):
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  username = forms.CharField(required=True)
  password1= forms.CharField(required=True)
  password2= forms.CharField(required=True)
  class Meta:
    model = User
    fields = ['first_name','last_name','email','username','password1','password2']
  
  def save(self, commit = True): 
      user = super(NurseUserForm, self).save(commit=False)
      user.email = self.cleaned_data['email']
      if commit:
        user.save()
      
      return user