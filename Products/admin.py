from django.contrib import admin

from django.contrib import admin
from Products.models import Products

# Register your models here.

class All_Products(admin.ModelAdmin):
    listOfProducts = (' products_Img ', 'products_Name',' products_Availability', 'products_Price ', 'products_Description')

admin.site.register(Products, All_Products)
 