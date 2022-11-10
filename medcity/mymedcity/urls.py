from django.urls import path
from . import views
from .views import book_appoinmet, pharma_add_med, intro, get_started, patient_home, admin_home, doctor_home, success, receptionist_home, patient_dashboard, aboutus, a_aboutus, d_aboutus, r_aboutus, p_aboutus, n_aboutus, appo_success, doctor_dashboard, receptionist_dashboard, pharmacy_home, nurse_home, admin_dashboard, pharmacy_dashboard, nurse_dashboard, pharma_update_med, pharma_view_med, doctor_view_med


app_name='mymedcity'

urlpatterns = [
  path('',get_started, name='get_started'),
  path('intro/',intro, name='intro'),
  
  path('patient_home/',patient_home, name='patient_home'),
  path('admin_home/',admin_home, name='admin_home'),
  path('doctor_home/',doctor_home, name='doctor_home'),
  path('receptionist_home/',receptionist_home, name='receptionist_home'),
  path('pharmacy_home/',pharmacy_home, name='pharmacy_home'),
  path('nurse_home/',nurse_home, name='nurse_home'),
  
  path('success/',success,name='success'),
  path('appo_success/',appo_success,name='appo_success'),
  
  path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
  path('patient_dashboard/',patient_dashboard,name='patient_dashboard'),
  path('doctor_dashboard/',doctor_dashboard,name='doctor_dashboard'),
  path('receptionist_dashboard/',receptionist_dashboard,name='receptionist_dashboard'),
  path('pharmacy_dashboard/',pharmacy_dashboard,name='pharmacy_dashboard'),
  path('nurse_dashboard/',nurse_dashboard,name='nurse_dashboard'),
  
  path('aboutus/',aboutus,name='aboutus'),
  path('a_aboutus/',a_aboutus,name='a_aboutus'),
  path('d_aboutus/',d_aboutus,name='d_aboutus'),
  path('r_aboutus/',r_aboutus,name='r_aboutus'),
  path('p_aboutus/',p_aboutus,name='p_aboutus'),
  path('n_aboutus/',n_aboutus,name='n_aboutus'),
  
  path('book_appoinment/',book_appoinmet,name='book_appoinment'),
  path('pharma_add_med/',pharma_add_med,name='pharma_add_med'),
  path('pharma_update_med/<int:id>',pharma_update_med,name='pharma_update_med'),
  path('pharma_view_med/',pharma_view_med,name='pharma_view_med'),
  path('doctor_view_med/',doctor_view_med,name='doctor_view_med'),

   
]