from django.db import models
from django.contrib.auth.models import User
from django.http import request
from phonenumber_field.modelfields import PhoneNumberField

from django.utils import timezone

# Create your models here.

class UserRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField()
    location=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class EmployeeRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField()
    location=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    available='available'
    not_available='not_available'
    availabilty_statuses=[
        (available,'available'),
        (not_available,'not_available')
    ]
    availabilty_status=models.CharField(max_length=50,choices=availabilty_statuses,default=available)
    def __str__(self):
        return str(self.user.username)






class BatteryBrand(models.Model):
    brand=models.CharField(max_length=50)
    def __str__(self):
        return str(self.brand)


class BatteryType(models.Model):
    type=models.CharField(max_length=50)
    brand=models.ForeignKey(BatteryBrand,on_delete=models.CASCADE,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.type)



class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    employee=models.ForeignKey(EmployeeRegister,on_delete=models.CASCADE,null=True,blank=True)
    user_details=models.ForeignKey(UserRegister,on_delete=models.CASCADE,null=True,blank=True)
    location=models.CharField(max_length=50)
    wanted_date=models.DateField(default=timezone.now)
    processing='processing'
    accepted='accepted'
    rejected='rejected'
    booking_statuses=[
        
        (processing,'processing'),
        (accepted,'accepted'),
        (rejected,'rejected')

    ]
    booking_status=models.CharField(max_length=50,choices=booking_statuses,default=processing)
    
    battery_type=models.ForeignKey(BatteryType,on_delete=models.CASCADE,null=True,blank=True)
    battery_brand=models.ForeignKey(BatteryBrand,on_delete=models.CASCADE,null=True,blank=True)
    unit=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    amount=models.IntegerField(default=500)
    paid=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)



class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    employee=models.ForeignKey(EmployeeRegister,on_delete=models.CASCADE,null=True,blank=True)
    user_details=models.ForeignKey(UserRegister,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)

    


