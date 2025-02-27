from django.urls import path, include 
from .views import pharmacy_list
from .views import pharmacy_detail
from .views import (
    medicine_list,medicine_detail ,order_list,order_detail ,create_order ,
    pharmacy_api ,signup,login_view,customer_dashboard,logout_view,pharmacy_dashboard,
    home_redirect
)

urlpatterns = [
   
   path('pharmacy_list/', pharmacy_list, name='pharmacy_list'),
   path('pharmacy_detail/<int:pk>/', pharmacy_detail, name='pharmacy_detail'),
   path('medicine_list/', medicine_list, name='medicine_list'),
   path('medicine_detail/<int:pk>/', medicine_detail, name='medicine_detail'),
   path('order_list/', order_list, name='order_list'),
   path('order_detail/<int:pk>/', order_detail, name='order_detail'),
   path('create_order/', create_order, name='create_order'),
   path('api/pharmacies/', pharmacy_api, name='pharmacy_api'),
   path('signup/', signup, name='signup'),
   path('login/', login_view, name='login'),
   path('customer_dashboard/', customer_dashboard, name='dashboard'),
   path('logout/', logout_view, name='logout'),
   path('pharmacy_dashboard/', pharmacy_dashboard, name='pharmacy_dashboard'),
   path('', home_redirect, name='home')
]

