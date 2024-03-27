from django.contrib import admin

from .models import Patient
from .models import Address
admin.site.register(Patient)
admin.site.register(Address)