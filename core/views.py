from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Service, Apartment
from .serializers import ServiceSerializer, ApartmentSerializer

# Create your views here.

class ServiceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ApartmentViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
