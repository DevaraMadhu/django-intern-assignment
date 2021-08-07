from django.forms import widgets
from .models import PatientList,DoctorList
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientList
        fields = '__all__'

        widgets = {
            'started_meds':DateInput()
        }
