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
    


