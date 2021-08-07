from django.contrib import admin
from .models import DoctorList,PatientList
# Register your models here.

admin.site.register(DoctorList)
admin.site.register(PatientList)
