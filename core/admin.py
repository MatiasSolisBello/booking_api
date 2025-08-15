from django.contrib import admin
from .models import Apartment, Availability, Service

# Register your models here.
admin.site.register([
    Apartment, Availability, Service
])
