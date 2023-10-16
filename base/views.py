from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Patient
from .forms import PatientForm

def index(request):
    patient_list = Patient.objects.order_by('last_name', 'first_name')
    context = {'patient_list': patient_list}
    return render(request, 'base/patient_list.html', context)

def detail(request, Patient_id):
    patient = Patient.objects.get(id=Patient_id)
    context = {'patient' : patient}
    return render(request, 'base/patient_detail.html',context)

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('base:index')
    else:
        form = PatientForm()
    context = {'form': form}
    return render(request, 'base/patient_form.html', context)
