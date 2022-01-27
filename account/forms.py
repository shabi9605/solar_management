from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        labels=('password1','password','password2','confirm password')


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=('phone','location')



class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model=EmployeeRegister
        fields=('phone','location')


class BookingForm(forms.ModelForm):
    
    wanted_date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Booking
        fields=('location','wanted_date','battery_type','battery_brand','unit')



class BookingFormUpdate(forms.ModelForm):
    
    class Meta:
        model=Booking
        fields=('booking_status','amount')

    
class ComplaintForm(forms.ModelForm):
    complaint=forms.Textarea()
    class Meta:
        model=Complaint
        fields=('complaint',)



class EstimateForm(forms.ModelForm):
    watt=forms.IntegerField()
    class Meta:
        model=BatteryType
        fields=('type','brand','watt')





class AvailabilityForm(forms.ModelForm):
    class Meta:
        model=EmployeeRegister
        fields=('availabilty_status',)