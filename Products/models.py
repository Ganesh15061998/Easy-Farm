from django.db import models
from django.db import models

class Products(models.Model):
    products_Img = models.ImageField(upload_to='image/')
    products_Name = models.CharField(max_length=50)
    products_Availability = models.CharField(max_length=50)
    products_Price = models.CharField(max_length=20)
    products_Description = models.TextField()

# Create your models here.
