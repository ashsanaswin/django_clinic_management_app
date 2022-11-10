from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from . import forms,models
from .models import Doctor
from .forms import NewUserForm,ReceptionUserForm,DoctorForm,DoctorUserForm,PharmacyUserForm,NurseUserForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect









def admin_add_doctor(request):
  userForm = forms.DoctorUserForm()
  doctorForm = forms.DoctorForm()
  mydict = {'userForm':userForm,'doctorForm':doctorForm}
  if request.method=='POST':
    userForm = forms.DoctorUserForm(request.POST)
    doctorForm = forms.DoctorForm(request.POST,request.FILES)
    if userForm.is_valid() and doctorForm.is_valid():
      user = userForm.save()
      user.set_password(user.password)
      user.save()
      doctor = doctorForm.save(commit=False)
      doctor.user=user
      doctor=doctor.save()
      doctor_group = Group.objects.get(name='Doctors') 
      user.groups.add(doctor_group)
      login(request,user)
    return HttpResponseRedirect('/doctor_home')
  return render(request,'users/admin_add_doctor.html',context=mydict)

def admin_add_reception(request):
  user ="none"
  if request.method == 'POST':
      form = ReceptionUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='Receptionist')
        user.groups.add(group)
        user.save()
        login(request,user)
        return redirect("/receptionist_home")
  
  else:
     form = ReceptionUserForm(request.POST)

  context = {
        'form': form,
    }

  return render(request, 'users/admin_add_reception.html', context)



def admin_add_pharma(request):
  user ="none"
  if request.method == 'POST':
      form = PharmacyUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='Pharmacy')
        user.groups.add(group)
        user.save()
        login(request,user)
        return redirect("/pharmacy_home")
  
  else:
     form = PharmacyUserForm(request.POST)

  context = {
        'form': form,
    }

  return render(request, 'users/admin_add_pharma.html', context)



def admin_add_nurse(request):
  user ="none"
  if request.method == 'POST':
      form = NurseUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='Nurse')
        user.groups.add(group)
        user.save()
        login(request,user)
        return redirect("/nurse_home")
  
  else:
     form = NurseUserForm(request.POST)

  context = {
        'form': form,
    }

  return render(request, 'users/admin_add_nurse.html', context)



# def staff_login_page(request):
#   if not request.user.is_authenticated:
    
#     if request.method == "POST":
#       form = AuthenticationForm(request,data=request.POST)
#       if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#           #users_in_group = Group.objects.get(name='Receptionist').user_set.all()
#           # if users_in_group=='Doctors':
#           #   login(request,user) 
            
#           #   return redirect("/doctor_home")
#           #if user in users_in_group:
#             login(request,user)
#             return redirect('/receptionist_home')
#         else:
#             return redirect("/intro")
#     else:
#       form=AuthenticationForm()  
#     return render(request,'users/staff_login.html',{'form':form})
#   else:
#     return HttpResponseRedirect("/intro")


def create_account_page(request):   #for patients to create their own account
  user ="none"
  if request.method == 'POST':
      form = NewUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        group = Group.objects.get(name='Patients')
        user.groups.add(group)
        user.save()
        login(request,user)
        return redirect("/patient_home")
  
  else:
     form = NewUserForm(request.POST)

  context = {
        'form': form,
    }

  return render(request, 'users/create_account.html', context)


def login_page(request): #patient's login page
  if not request.user.is_authenticated:
    users_in_group = Group.objects.get(name="Patients").user_set.all()
    if request.method == "POST":
      form = AuthenticationForm(request,data=request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
          if user in users_in_group:
            login(request,user)
            return redirect("/patient_home")
          else:
            return redirect("/intro")
    else:
      form=AuthenticationForm()  
    return render(request,'users/login.html',{'form':form})
  else:
    return HttpResponseRedirect("/intro")



def admin_login(request):
  if not request.user.is_authenticated:
    users_in_group = Group.objects.get(name="Admin").user_set.all()
    if request.method == "POST":
      form = AuthenticationForm(request,data=request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
          if user in users_in_group:
            login(request,user)
            return redirect("/admin_home")
          else:
            return redirect("/intro")
    else:
      form=AuthenticationForm()  
    return render(request,'users/admin_login.html',{'form':form})
  else:
    return HttpResponseRedirect("/intro")

def patient_view_doctor(request):
    doc = Doctor.objects.all()

    context = {
        'doc': doc
    }

    return render(request, 'users/patient_view_doctor.html', context)

def a_view_doctor(request):
    doc = Doctor.objects.all()

    context = {
        'doc': doc
    }

    return render(request, 'users/a_view_doctor.html', context)

def r_view_doctor(request):
    doc = Doctor.objects.all()

    context = {
        'doc': doc
    }

    return render(request, 'users/r_view_doctor.html', context)



