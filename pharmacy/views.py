from django.shortcuts import render, redirect 
from django.http import JsonResponse
from .models import Pharmacy
from .models import Medicine
from .models import Order
from .models import OrderItem
from .forms import OrderForm

from django.shortcuts import get_object_or_404 

# Create your views here.
def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'pharmacy/pharmacy_list.html', {'pharmacies': pharmacies})


def pharmacy_detail(request, pk):
    pharmacy = get_object_or_404(Pharmacy, pk=pk)
    return render(request, 'pharmacy/pharmacy_detail.html', {'pharmacy': pharmacy})


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})

def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'pharmacy/medicine_detail.html', {'medicine': medicine})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pharmacy/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk) 
    return render(request, 'pharmacy/order_detail.html', {'order': order})

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