from .models import Service, Apartment
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
        
class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
    