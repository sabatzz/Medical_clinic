from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Address
from .forms import PatientForm, AddressForm

import logging
logger = logging.getLogger(__name__)


def patient_list(request):
    sort_by = request.GET.get('sort_by')
    #download data from models
    patients = Patient.objects.all()
    addresses = Address.objects.all()

        #sorting
    if sort_by == 'first_name_asc':
        patients = patients.order_by('first_name')
    elif sort_by == 'first_name_desc':
        patients = patients.order_by('-first_name')
    elif sort_by == 'last_name_asc':
        patients = patients.order_by('last_name')
    elif sort_by == 'last_name_desc':
        patients = patients.order_by('-last_name')

        #assigning addresses to patients
    for patient in patients:
        patient.address = addresses.filter(patient=patient).first()

        #searching
    search_query = request.GET.get('search')
    if search_query:
        patients = patients.filter(first_name__icontains=search_query) | patients.filter(last_name__icontains=search_query)

    patient_form = PatientForm()
    address_form = AddressForm()

    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        address_form = AddressForm(request.POST)
        if patient_form.is_valid() and address_form.is_valid():
            patient = patient_form.save()
            address = address_form.save(commit=False)
            address.patient = patient
            address.save()
            return redirect('patients:patient_list')

    return render(request, 'patients/patient_list.html', {'patients': patients, 'patient_form': patient_form, 'address_form': address_form})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    address = patient.address_set.first()
    print(address)
    logger.info(address)
    return render(request, 'patients/patient_detail.html', {'patient': patient, 'address': address})


def patient_new(request):
    if request.method == "POST":
        patient_form = PatientForm(request.POST)
        address_form = AddressForm(request.POST)
        if patient_form.is_valid() and address_form.is_valid():
            patient = patient_form.save()
            address = address_form.save(commit=False)
            address.patient = patient
            address.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        patient_form = PatientForm()
        address_form = AddressForm()
    return render(request, 'patients/patient_edit.html', {'patient_form': patient_form, 'address_form': address_form})

def edit_patient_and_address(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    address = patient.address_set.first()
    if request.method == "POST":
        patient_form = PatientForm(request.POST, instance=patient)
        address_form = AddressForm(request.POST, instance=address)
        if patient_form.is_valid() and address_form.is_valid():
            patient_form.save()
            address_form.save()
            return redirect('patients:patient_list')  #redirect to the main view
    else:
        patient_form = PatientForm(instance=patient)
        address_form = AddressForm(instance=address)
    return render(request, 'patients/edit_patient_and_address.html',
                  {'patient_form': patient_form, 'address_form': address_form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients:patient_list')  # redirect to the main view
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})
