from django.forms.forms import Form
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import PatientList,DoctorList
from django.contrib import messages
from .forms import PatientForm


# Create your views here.
def homepage(request):
    template_name = 'homepage.html'
    patients_data = PatientList.objects.all()
    return  render(request,template_name,{'patients_list':patients_data})

def delete_pat(request):
    id = request.POST.get('id')
    patients_data = PatientList.objects.get(id=id).delete()
    return JsonResponse({"message":"pateitnt is deleted"})

def update_pat(request,id):
    template_name = 'updateform.html'
    patient_obj  = PatientList.objects.get(id=id)
    if request.method == 'POST':
        update_form = PatientForm(request.POST,instance=patient_obj)
        if update_form.is_valid():
            update_form.save()
            messages.success(request,'fileds Updated')
            # return redirect('/home')
    update_form = PatientForm(instance=patient_obj)
    return render(request,template_name,{'form':update_form})


def create_pat(request):
    template_name = 'createform.html'
    update_form = PatientForm()
    if request.method == 'POST':
        update_form = PatientForm(request.POST)
        if update_form.is_valid():
            update_form.save()
            messages.success(request,'Patient form created')
            # return redirect('/home')
    return render(request,template_name,{'form':update_form})
