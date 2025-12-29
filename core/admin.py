from django.contrib import admin
from .models import Apartment, ApartmentImages, ApartmentService, Availability, Booking, Service

# Register your models here.
class ApartmentImagesInline(admin.TabularInline):
    model = ApartmentImages
    extra = 1

class ApartmentServiceInline(admin.TabularInline):
    model = ApartmentService
    extra = 1


class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImagesInline, ApartmentServiceInline] 
    
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register([Booking, Service])
