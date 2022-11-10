from django.urls import path
from .views import admin_add_reception, admin_login, create_account_page, patient_view_doctor, login_page , admin_add_doctor,admin_add_pharma,admin_add_nurse,a_view_doctor,r_view_doctor  #staff_login_page
from django.contrib.auth import views as authentication_views


app_name='users'

urlpatterns = [
  path('createaccount/',create_account_page, name='create_account_page'),
  path('login/',login_page, name='login_page'),
  path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
  path('admin_login/',admin_login, name='admin_login'),
  path('admin_add_doctor/',admin_add_doctor, name='admin_add_doctor'),
  path('admin_add_reception/',admin_add_reception, name='admin_add_reception'),
  path('admin_add_pharma/',admin_add_pharma, name='admin_add_pharma'),
  path('admin_add_nurse/',admin_add_nurse, name='admin_add_nurse'),
  #path('staff_login_page/',staff_login_page, name='staff_login_page'),
  path('staff_login/',authentication_views.LoginView.as_view(template_name='users/staff_login.html'),name='staff_login'),
  path('patient_view_doctor/',patient_view_doctor, name='patient_view_doctor'),
  path('a_view_doctor/',a_view_doctor, name='a_view_doctor'),
  path('r_view_doctor/',r_view_doctor, name='r_view_doctor'),
]