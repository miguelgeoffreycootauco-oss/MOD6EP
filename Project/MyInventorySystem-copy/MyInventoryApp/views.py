from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, WaterBottle, Account

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

def manage_account(request, pk):
    account_obj = get_object_or_404(Account, pk=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {'account': account_obj})

def delete_account(request, pk):
    account_obj = get_object_or_404(Account, pk=pk)
    account_obj.delete()
    if 'user_id' in request.session:
        del request.session['user_id']
        
    return redirect('login')

def change_password(request, pk):
    account_obj = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        account_obj.password = new_password
        account_obj.save()
        return redirect('manage_account', pk=pk)
    
    return render(request, 'MyInventoryApp/change_password.html', {'account': account_obj})

def login_view(request): 
    if request.method == "POST": 
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        account = Account.objects.filter(username = username, password = password)
        if account: 
            return redirect('view_supplier') 
        else: 
            return render(request, 'MyInventoryApp/login.html', {'error_message': 'Invalid login'})
    return render(request, 'MyInventoryApp/login.html')

def signup(request): 
    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        existing= Account.objects.filter(username=username) 
        if existing: 
            return render(request, 'MyInventoryApp/signup.html', {'error_message': 'Account already exists'})
        else: 
            Account.objects.create(username = username, password = password) 
            return render(request, 'MyInventoryApp/login.html', {'success_message': 'Account created successfully'}) 
    return render(request, 'MyInventoryApp/signup.html')

    