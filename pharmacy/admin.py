from django.contrib import admin
from .models import Pharmacy  , Medicine , Order , OrderItem

# Register your models here.
admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(OrderItem)