from django import forms
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'customer_contact', 'customer_address', 
                  'pharmacy', 'delivery_method']
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name']
        