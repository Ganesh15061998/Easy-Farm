from django.db import models
from django.db import models

# Create your models here.

class Registration(models.Model):
    registar_Fname = models.CharField(max_length=50)
    registar_Email = models.EmailField()
    registar_Mobile = models.IntegerField(max_length=10)
    registar_Dob = models.DateField()
    registar_Password = models.CharField(max_length=250)
    registar_ConfmPassword = models.CharField(max_length=250)
    

