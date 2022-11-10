from django.contrib import admin
from django.contrib import admin
from users.models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
  pass

admin.site.register(Doctor,DoctorAdmin)