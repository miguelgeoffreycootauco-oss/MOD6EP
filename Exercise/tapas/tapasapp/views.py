from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish 
from .models import Account

# Create your views here.

current_account_pk = 0
def better_menu(request, pk):
    global current_account_pk
    current_account_pk = pk
    account = get_object_or_404(Account, pk=pk) 
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/better_list.html', {'dishes':dish_objects, 'account': account})

def add_menu(request):
    if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu', pk=current_account_pk)
    else:
        return render(request, 'tapasapp/add_menu.html', {'current_account_pk': current_account_pk})

def view_detail(request, pk):
    d = get_object_or_404(Dish, pk=pk)
    return render(request, 'tapasapp/view_detail.html', {'d': d, 'current_account_pk': current_account_pk})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('better_menu', pk=current_account_pk)

def update_dish(request, pk):
    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', pk=pk)
    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_menu.html', {'d':d, 'current_account_pk': current_account_pk})

def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = Account.objects.filter(username=username, password=password)
        if account: 
            a = Account.objects.get(username=username, password=password)
            return redirect('better_menu', pk = a.pk)
        else:
            error_message = 'Invalid login.'
    return render(request, 'tapasapp/login.html', {'error_message': error_message})

def signup_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Account.objects.filter(username=username).exists():
            error_message = 'Account already exists.'
        else:
            Account.objects.create(username=username, password=password)
            error_message = 'Account created successfully.'
            return redirect('login')

    return render(request, 'tapasapp/signup.html', {'error_message': error_message})

def manage_account(request, pk): 
    account = get_object_or_404(Account, pk = pk)
    return render(request, 'tapasapp/manage_account.html', {'account': account, 'current_account_pk': current_account_pk})
 
