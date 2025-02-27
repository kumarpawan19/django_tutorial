from django.shortcuts import render, redirect 
from django.http import JsonResponse
from .models import Pharmacy
from .models import Medicine
from .models import Order
from .models import OrderItem
from .forms import OrderForm,SignUpForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404 

# Create your views here.
def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'pharmacy/pharmacy_list.html', {'pharmacies': pharmacies})



def pharmacy_detail(request, pk):
    pharmacy = get_object_or_404(Pharmacy, pk=pk)
    return render(request, 'pharmacy/pharmacy_detail.html', {'pharmacy': pharmacy})




@login_required(login_url='/pharmacy/login/')
def medicine_list(request):
    medicines = Medicine.objects.all()

    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})

@login_required(login_url='/pharmacy/login/')
def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'pharmacy/medicine_detail.html', {'medicine': medicine})

@login_required(login_url='/pharmacy/login/')
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pharmacy/order_list.html', {'orders': orders})

@login_required(login_url='/pharmacy/login/')
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk) 
    return render(request, 'pharmacy/order_detail.html', {'order': order})

@login_required(login_url='/pharmacy/login/')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
        else:
            print(form.errors)
    else:
        form = OrderForm()
    return render(request, 'pharmacy/create_order.html', {'form': form})
    

def pharmacy_api(request):
    pharmacies = Pharmacy.objects.all().values('id', 'name', 'address', 'phone')
    return JsonResponse({'pharmacies': list(pharmacies)})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # login the user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print('login successful')

            if user.groups.filter(name='pharmacist').exists():
                return redirect('pharmacy_dashboard')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html',{'form': form})


@login_required(login_url='/pharmacy/login/')
def customer_dashboard(request):
    return render(request, 'pharmacy/customer_dashboard.html')

@login_required(login_url='/pharmacy/login/')
def pharmacy_dashboard(request):
    return render(request, 'pharmacy/pharmacy_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def home_redirect(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='pharmacist').exists():
            return redirect('pharmacy_dashboard')
        return redirect('dashboard')
    return redirect('/')


