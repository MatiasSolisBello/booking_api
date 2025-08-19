from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Service, Apartment
from .serializers import BookingSerializer, ServiceSerializer, ApartmentSerializer

# Create your views here.

class ServiceViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    
class ApartmentViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    
class BookingViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

    
