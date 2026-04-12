from django.shortcuts import render
from .models import Supplier, WaterBottle

# Create your views here.

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier.html', {'suppliers': suppliers})

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/bottles.html', {'bottles': bottles})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')

