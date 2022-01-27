from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# Create your views here.
def index(request):
    battery=BatteryType.objects.all()
    print(battery)
    if request.method=="POST":
        type=request.POST.get('type')
        brand=request.POST.get('brand')
        watt=request.POST.get('watt')
        try:
            battery_price=BatteryType.objects.get(type=type,brand=brand)
            print(battery_price.price)
            estimate_price=int(watt)*3+int(battery_price.price)
            print(estimate_price)
            battery=BatteryType.objects.all()
            return render(request,'index.html',{'battery':battery,'estimate_price':estimate_price})
        except:
            return render(request,'index.html',{'battery':battery})


    return render(request,'index.html',{'battery':battery})


def user_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        user_registration_form=UserRegistrationForm(data=request.POST)
        if user_form.is_valid() and user_registration_form.is_valid():
            user=user_form.save()
            user.save()
            profile=user_registration_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         user_registration_form=UserRegistrationForm()
    return render(request,'user_register.html',{'register':reg,'user_form':user_form,'user_registration_form':user_registration_form})



def employee_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        employee_registration_form=EmployeeRegistrationForm(data=request.POST)
        if user_form.is_valid() and employee_registration_form.is_valid():
            user=user_form.save()
            user.save()
            profile=employee_registration_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         employee_registration_form=EmployeeRegistrationForm()
    return render(request,'employee_register.html',{'register':reg,'user_form':user_form,'employee_registration_form':employee_registration_form})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        try:
            user1=UserRegister.objects.get(user=user)
            print(user1)
        except:
            pass
            
        try:
            user2=EmployeeRegister.objects.get(user=user)
        except:
            pass

        if user:
            if user.is_active:
                try:
                    if user1:
                        active=UserRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if user2:
                        active=EmployeeRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if user.is_superuser:
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass                
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else: 
        return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    return render(request,'dashboard.html')



def booking_services(request):
    
    if request.method=="POST":
        booking_form=BookingForm(request.POST)
        if booking_form.is_valid():
            user_details=UserRegister.objects.get(user=request.user)
            print(user_details)
            cp=Booking(user=request.user,user_details=user_details,location=booking_form.cleaned_data['location'],wanted_date=booking_form.cleaned_data['wanted_date'],
            battery_type=booking_form.cleaned_data['battery_type'],battery_brand=booking_form.cleaned_data['battery_brand'],unit=booking_form.cleaned_data['unit'])
            cp.save()

            
            return render(request,'booking_form.html',{'msg':'successfully added request'})
        else:
            return HttpResponse("Invalid form")
    booking_form=BookingForm()
    return render(request,'booking_form.html',{'form':booking_form})



def view_service_booking(request):
    bookings=Booking.objects.filter(employee=None).order_by('-id')
    return render(request,'view_all_bookings.html',{'bookings':bookings})


def my_bookings(request):
    my_booking=Booking.objects.filter(user=request.user)
    print(my_booking)
    return render(request,'my_bookings.html',{'my_booking':my_booking})


def allotted_work(request):
    
    employee=EmployeeRegister.objects.get(user=request.user)
    try:
        my_work=Booking.objects.filter(employee=employee)
    except:
        pass
    return render(request,'my_works.html',{'my_work':my_work})


def send_complaint(request):
    if request.method=="POST":
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
            user_details=UserRegister.objects.get(user=request.user)
            print(user_details)
            cp=Complaint(user=request.user,user_details=user_details,complaint=complaint_form.cleaned_data['complaint'])
            cp.save()

            
            return render(request,'complaint_form.html',{'msg':'successfully added request'})
        else:
            return HttpResponse("Invalid form")
    complaint_form=ComplaintForm()
    return render(request,'complaint_form.html',{'form':complaint_form})



def my_complaints(request):
    my_complaint=Complaint.objects.filter(user=request.user)
    print(my_complaint)
    return render(request,'my_complaint.html',{'my_complaint':my_complaint})


def allotted_complaints(request):
    employee=EmployeeRegister.objects.get(user=request.user)
    try:
        my_complain=Complaint.objects.filter(employee=employee)
    except:
        pass
    return render(request,'allotted_complaint.html',{'my_complain':my_complain})





def assign_employee(request,id):
    available_employees=EmployeeRegister.objects.filter(availabilty_status='available')
    booking=Booking.objects.get(id=id)
    if request.method=="POST":
        available_employees=EmployeeRegister.objects.filter(availabilty_status='available')
        
        employee=request.POST.get('employee')
        print(employee)
        employee=EmployeeRegister.objects.get(id=employee)
        requirement=Booking.objects.update_or_create(id=id,
        defaults={'employee':employee}
        )
        return redirect('view_service_booking')

    return render(request,'assign_employee.html',{'available_employees':available_employees})



def update_booking(request,id):
    booking=Booking.objects.get(id=id)
    print(booking)
    update_booking_form=BookingFormUpdate(instance=booking)
    if request.method=="POST":
        update_booking_form=BookingFormUpdate(request.POST,request.FILES,instance=booking)
        update_booking_form.save()
        return redirect('allotted_work')
    return render(request,'booking_form.html',{'form':update_booking_form})



def change_status(request):
    my_volunteer=EmployeeRegister.objects.get(user=request.user)
    print(my_volunteer.availabilty_status)
    if request.method=="POST":
        my_volunteer=EmployeeRegister.objects.get(user=request.user)
        update_form=AvailabilityForm(request.POST,instance=my_volunteer)
        #print(my_volunteer.availability_status)
        if update_form.is_valid():
            update_form.save()
            
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=AvailabilityForm(instance=my_volunteer.user)
        
    context={
        'update_form':update_form,
        
    }
    return render(request,'update_employee_availability.html',context)



def estimate_price(request):
    battery=BatteryType.objects.all()
    print(battery)
    # if request.method=="POST":


        
        
           
            

            
        
   
    return render(request,'index.html',{'battery':battery})


