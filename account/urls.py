from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('user_register',views.user_register,name='user_register'),
    path('employee_register',views.employee_register,name='employee_register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('dashboard',views.dashboard,name='dashboard'),


    path('booking_services',views.booking_services,name='booking_services'),
    path('my_bookings',views.my_bookings,name='my_bookings'),
    path('allotted_work',views.allotted_work,name='allotted_work'),

    path('send_complaint',views.send_complaint,name='send_complaint'),
    path('my_complaints',views.my_complaints,name='my_complaints'),
    path('allotted_complaints',views.allotted_complaints,name='allotted_complaints'),


    path('view_service_booking',views.view_service_booking,name='view_service_booking'),

    path('assign_employee/<int:id>',views.assign_employee,name='assign_employee'),

    path('update_booking/<int:id>',views.update_booking,name='update_booking'),
    path('change_status',views.change_status,name='change_status'),

    

    

]