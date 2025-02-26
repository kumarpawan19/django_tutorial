from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()  

    def __str__(self):
        return self.name + ' - ' + self.address
    
    
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()  

    pharmacies = models.ManyToManyField(Pharmacy, related_name='medicines')

    def __str__(self):
        return self.name + ' - ' + str(self.price)
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    DELIVERY_CHOICES = [
        ('CLICK_COLLECT', 'Click and Collect'),
        ('HOME_DELIVERY', 'Home Delivery'),
    ]
    
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=100)
    customer_address = models.TextField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.SET_NULL, null=True, related_name='orders')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_CHOICES)


    def __str__(self):
        return f"{self.customer_name} - {self.date_created.strftime('%Y-%m-%d')}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price_at_time = models.FloatField()

    def __str__(self):
        return f"{self.medicine.name} x{self.quantity} - Order #{self.order.id}"



