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
    if request.method == 'POST':
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouth_size = request.POST.get('mouth_size')
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')
        supplier = request.POST.get('supplier')

        WaterBottle.objects.create(
            sku=sku,
            brand=brand,
            cost=cost,
            size=size,
            mouth_size=mouth_size,
            color=color,
            quantity=quantity,
            supplier_id=supplier
        )
        return redirect('view_bottles')
    
    all_suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': all_suppliers})

