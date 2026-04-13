from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, WaterBottle, Account

# Create your views here.

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier.html', {
        'suppliers': suppliers,
        'current_user_id': request.session.get('user_id')
    })

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/bottles.html', {
        'bottles': bottles,
        'current_user_id': request.session.get('user_id')
    })

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
    return render(request, 'MyInventoryApp/add_bottle.html', {
        'suppliers': all_suppliers,
        'current_user_id': request.session.get('user_id') # ADD THIS
    })
    
def manage_account(request, pk):
    if not request.session.get('user_id'):
        return redirect('login')
        
    account_obj = get_object_or_404(Account, pk=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {
        'account': account_obj,
        'current_user_id': request.session.get('user_id')
    })

def change_password(request, pk):
    account_obj = get_object_or_404(Account, pk=pk)
    error = None

    if request.method == 'POST':
        current_p = request.POST.get('current_password')
        new_p = request.POST.get('new_password')
        confirm_p = request.POST.get('confirm_password')

        if account_obj.password != current_p:
            error = "Current password is incorrect."
        
        elif new_p != confirm_p:
            error = "New passwords do not match."
            
        else:
            account_obj.password = new_p
            account_obj.save()
            return redirect('manage_account', pk=pk)
    
    return render(request, 'MyInventoryApp/change_password.html', {
        'account': account_obj,
        'error': error,
        'current_user_id': request.session.get('user_id')
    })

def delete_account(request, pk):
    account_obj = get_object_or_404(Account, pk=pk)
    account_obj.delete()
    if 'user_id' in request.session:
        del request.session['user_id']
        
    return redirect('login')

def login_view(request): 
    if request.method == "POST": 
        u = request.POST.get('username') 
        p = request.POST.get('password') 
        account_results = Account.objects.filter(username=u, password=p)
        
        if account_results.exists(): 
            user_obj = account_results.first()
            request.session['user_id'] = user_obj.id 
            return redirect('view_bottles') 
        else: 
            return render(request, 'MyInventoryApp/login.html', {'error': 'Invalid login'})
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

def index(request): # Or whatever your root view is named
    return render(request, 'MyInventoryApp/index.html', {
        'current_user_id': request.session.get('user_id')
    })