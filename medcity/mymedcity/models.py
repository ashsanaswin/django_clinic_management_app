from django.db import models
from django.contrib.auth.models import User
# Create your models here.
departments=[('Cardiologist','Cardiologist'),
('Emergency Medicin Specialist','Emergency Medicin Specialist'),
('ENT Specialist','ENT Specialist'),('Surgeons','Surgeons'),
('Eye Specialist','Eye Specialist'),('Scaning Testing and Others','Scaning Testing and Others')
]

times = [('10am to 11pm','10am to 11pm'),
         ('11am to 12pm','11am to 12pm'),
         ('2pm to 3pm','2pm to 3pm'),
         ('3pm to 4pm','3pm to 4pm')
]


class Appoinment(models.Model):
  def __str__(self):
        return self.first_name
  user =models.OneToOneField(User,on_delete=models.CASCADE, default=10)
  first_name   = models.CharField(max_length=20)
  last_name    = models.CharField(max_length=20)
  email        = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=10)
  date         = models.DateField(max_length=10)
  time         = models.TimeField(max_length=50 ,choices=times, default='10am to 11pm' )
  department   = models.CharField(max_length=50,choices=departments,default='Cardiologist')

class Pharmacy(models.Model):
      def __str__(self):
        return self.name
      name = models.CharField(max_length=50,null=True,blank=True)
      price = models.IntegerField(null=True,blank=True)
      description = models.CharField(max_length=50,null=True,blank=True)
      dose = models.CharField(max_length=10,null= True, blank=True)
      dosage = models.CharField(max_length=50,null=True,blank=True)
      image = models.ImageField(blank=True, upload_to='image')
      mfg_date = models.DateField(max_length=10,null=True,blank=True)
      exp_date = models.DateField(max_length=10,null=True,blank=True)
      mfg_lic = models.CharField(max_length=50,null=True,blank=True)
