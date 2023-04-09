from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from Products.models import Products
from Vehicles.models import Vehivles


# def homePage(request):
#     return HttpResponse('<h1>HEool</h1>')

def homePage(request):
    serviceData = Products.objects.all()
   
    return render(request , 'Home.html',{'serviceData':serviceData})

def userProfile(request):
    return render(request , 'Profile.html')

def Categories(request):
    return render(request , 'Categories.html')

def Instrument(request):
    return render(request , 'instruments.html')

def Fertilizer(request):
    return render(request , 'Fertilizer.html')

def Vehicle(request):
    serviceData = Vehivles.objects.all()
    return render(request , 'Vehicle.html' ,{'serviceData':serviceData})

def Bokking(request):
    return render(request , 'Bokking.html')

def Setting(request):
    return render(request , 'Setting.html')

def Login(request):
    return render(request , 'Login.html')

def Registration(request):
    return render(request , 'Registration.html')