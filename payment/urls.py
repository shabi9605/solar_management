from django.urls import path
from .import views

app_name = 'payment'
urlpatterns = [
    path('payment/<int:booking_id>',views.payment,name='payment'),
    path('payment-status', views.payment_status, name='payment-status'),


 
    
]
