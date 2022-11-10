from django.db import models

from django.contrib.auth.models import User

departments=[('Cardiologist','Cardiologist'),
('Emergency Medicin Specialist','Emergency Medicin Specialist'),
('ENT Specialist','ENT Specialist'),('Surgeons','Surgeons'),
('Eye Specialist','Eye Specialist'),('Scaning Testing and Others','Scaning Testing and Others')
]

class Doctor(models.Model):
  user =models.OneToOneField(User,on_delete=models.CASCADE)
  
  phone_number = models.CharField(max_length=10)
  specialization = models.CharField(max_length=50)
  medical_degrees = models.CharField(max_length= 100)
  department = models.CharField(max_length=50,choices=departments,default='Cardiologist')

  @property
  def get_name(self):
    return self.user.first_name+" "+self.user.last_name

  @property
  def get_id(self):
    return self.user.id

  def __str__(self):
    return self.get_name
