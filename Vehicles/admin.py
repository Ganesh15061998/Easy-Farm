from django.contrib import admin

from django.contrib import admin
from Vehicles.models import Vehivles
# Register your models here.

class All_Vehicles(admin.ModelAdmin):
    LostOfVehicles = ( 'vahicle_Img',
' vahicle_Name',
 'vahicle_Availability',
 'vahicle_Price,'
 'vahicle_Description')

admin.site.register(Vehivles, All_Vehicles)
 