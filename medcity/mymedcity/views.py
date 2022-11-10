from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . forms import AppoForm
from .models import Appoinment,Pharmacy
from .decorators import check_user_able_to_see_page



def intro(request):
  return render(request,'mymedcity/intro.html')

def get_started(request):
  return render(request,'mymedcity/get_started.html')
#@check_user_able_to_see_page("Patients")



def patient_home(request):
  return render(request,'mymedcity/patient_home.html')

#@check_user_able_to_see_page("Admin")
def admin_home(request):
  return render(request,'mymedcity/admin_home.html')

#@check_user_able_to_see_page("Doctors")
def doctor_home(request):
  return render(request,'mymedcity/doctor_home.html')

#@check_user_able_to_see_page("Doctors")
def receptionist_home(request):
  return render(request,'mymedcity/receptionist_home.html')

#@check_user_able_to_see_page("Doctors")
def pharmacy_home(request):
  return render(request,'mymedcity/pharmacy_home.html')

#@check_user_able_to_see_page("Doctors")
def nurse_home(request):
  return render(request,'mymedcity/nurse_home.html')



def success(request):
  return render(request,'mymedcity/success.html')

def appo_success(request):
  return render(request,'mymedcity/appo_success.html')



def admin_dashboard(request):
  return render(request,'mymedcity/admin_dashboard.html')

def patient_dashboard(request):
  return render(request,'mymedcity/patient_dashboard.html')

def doctor_dashboard(request):
  return render(request,'mymedcity/doctor_dashboard.html')

def receptionist_dashboard(request):
  return render(request,'mymedcity/receptionist_dashboard.html')

def pharmacy_dashboard(request):
  return render(request,'mymedcity/pharmacy_dashboard.html')

def nurse_dashboard(request):
  return render(request,'mymedcity/nurse_dashboard.html')



def aboutus(request):
  return render(request,'mymedcity/aboutus.html')

def a_aboutus(request):
  return render(request,'mymedcity/a_aboutus.html')


def d_aboutus(request):
  return render(request,'mymedcity/d_aboutus.html')

def r_aboutus(request):
  return render(request,'mymedcity/r_aboutus.html')

def p_aboutus(request):
  return render(request,'mymedcity/p_aboutus.html')

def n_aboutus(request):
  return render(request,'mymedcity/n_aboutus.html')



def book_appoinmet(request):
  form = forms.AppoForm(request.POST)
  if request.method == 'POST':
    form = forms.AppoForm(request.POST)
    if form.is_valid():
      
      form.save()
        
      return redirect("/appo_success")

  else:
     form = AppoForm(request.POST)
  context = {
        'form': form,
    }
  return render(request,'mymedcity/book_appoinment.html',context)



def pharma_add_med(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    price = request.POST.get('price')
    desc = request.POST.get('desc')
    dose = request.POST.get('dose')
    dosage = request.POST.get('dosage')
    image = request.FILES['upload']
    mfg = request.POST.get('mfg')
    exp = request.POST.get('exp')
    mfg_lic = request.POST.get('mfg_lic')

    med = Pharmacy(name=name,price=price,description=desc,dose=dose,dosage=dosage,image=image,mfg_date=mfg,exp_date=exp,mfg_lic=mfg_lic)
    med.save()
    return redirect('/pharmacy_home')

  return render(request,'mymedcity/pharma_add_med.html')



def pharma_update_med(request,id):
  med = Pharmacy.objects.get(id=id)
  if request.method == 'Post':
    med.name = request.POST.get('name')
    med.price = request.POST.get('price')
    med.desc = request.POST.get('desc')
    med.dose = request.POST.get('dose')
    med.dosage = request.POST.get('dosage')
    med.mfg = request.POST.get('mfg')
    med.exp = request.POST.get('exp')
    med.mfg_lic = request.POST.get('mfg_lic')

    try:
        med.image = request.FILES['upload']
    except:
        pass

    med.save()
    return redirect('/pharmacy_home')
  
  context = {
      'med':med
    }
  return render(request,'mymedcity/pharma_update_med.html',context)



def pharma_view_med(request):
    med = Pharmacy.objects.all()

    context = {
        'med': med
    }

    return render(request, 'mymedcity/pharma_view_med.html', context)



def doctor_view_med(request):
    med = Pharmacy.objects.all()

    context = {
        'med': med
    }

    return render(request, 'mymedcity/doctor_view_med.html', context)
