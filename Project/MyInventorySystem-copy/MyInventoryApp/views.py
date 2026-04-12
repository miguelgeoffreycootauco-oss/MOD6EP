from django.shortcuts import render, redirect
from .models import Supplier, WaterBottle

# Create your views here.

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier.html', {'suppliers': suppliers})

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/bottles.html', {'bottles': bottles})

def add_bottle(request):
    if request.method == 'POST':
        sku_in = request.POST.get('sku')
        brand_in = request.POST.get('brand')
        cost_in = request.POST.get('cost')
        size_in = request.POST.get('size')
        mouth_size_in = request.POST.get('mouth_size')
        color_in = request.POST.get('color')
        quantity_in = request.POST.get('quantity')
        supplier_id_in = request.POST.get('supplier')
        supplier_obj = Supplier.objects.get(id=supplier_id_in)
        WaterBottle.objects.create(
            sku=sku_in, 
            brand=brand_in, 
            cost=cost_in, 
            size=size_in, 
            mouth_size=mouth_size_in, 
            color=color_in, 
            current_quantity=quantity_in, 
            supplied_by=supplier_obj
            )
        return redirect('view_bottles')
    
    all_suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': all_suppliers})

