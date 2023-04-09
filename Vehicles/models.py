from django.db import models
from django.db import models

class Vehivles(models.Model):
    vahicle_Img = models.ImageField(upload_to='media/image',default='')
    vahicle_Name = models.CharField(max_length=50)
    vahicle_Availability = models.CharField(max_length=50)
    vahicle_Price = models.CharField(max_length=20)
    vahicle_Description = models.TextField()

# Create your models here.
