from django.contrib import admin
from .models import Apartment, ApartmentService, Availability, Booking, Service

# Register your models here.
admin.site.register([
    Apartment, ApartmentService, Availability, Booking, Service
])
