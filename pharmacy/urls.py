from django.urls import path, include 
from .views import pharmacy_list
from .views import pharmacy_detail
from .views import medicine_list,medicine_detail

urlpatterns = [
   
   path('pharmacy_list/', pharmacy_list, name='pharmacy_list'),
   path('pharmacy_detail/<int:pk>/', pharmacy_detail, name='pharmacy_detail'),
   path('medicine_list/', medicine_list, name='medicine_list'),
   path('medicine_detail/<int:pk>/', medicine_detail, name='medicine_detail'),

]

