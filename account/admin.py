from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(UserRegister)
admin.site.register(EmployeeRegister)
admin.site.register(Booking)
admin.site.register(Complaint)
admin.site.register(BatteryType)
admin.site.register(BatteryBrand)

