import datetime
from django.db import models
from django.utils import timezone


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pesel = models.CharField(max_length=11)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, PESEL: {self.pesel}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def update_patient(self, first_name, last_name, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.save()


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

    def update_address(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.save()
