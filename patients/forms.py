from django import forms
from .models import Patient, Address
from datetime import date


class PatientForm(forms.ModelForm):
    pub_date = forms.DateField(initial=date.today)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'pesel', 'pub_date']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'zipcode']
