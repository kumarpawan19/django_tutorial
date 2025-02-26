from django.shortcuts import render
from .models import Pharmacy
from .models import Medicine
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