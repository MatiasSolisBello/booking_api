from .models import Booking, Service, Apartment, ApartmentService
from django.contrib.auth.models import User
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    '''
    Serializador de Servicio.
    '''
    class Meta:
        model = Service
        #fields = '__all__'
        fields = ['name', 'price', 'icon']
        
        
class ApartmentServiceSerializer(serializers.ModelSerializer):
    '''
    Serializador de la relación entre Departamento y Servicio.
    '''
    name = serializers.CharField(source='service.name')
    price = serializers.CharField(source='service.price')

    class Meta:
        model = ApartmentService
        fields = ['name', 'price']
    
    
class ApartmentSerializer(serializers.ModelSerializer):
    '''
    Serializador de Departamento.
    Incluye los servicios disponibles para el departamento.
    '''
    
    # Agregar datos del servicio relacionado al departamento
    services = ApartmentServiceSerializer(source='apartments', many=True)
    
    class Meta:
        model = Apartment
        fields = [
            'name',
            'city',
            'services',
        ]
        

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializador de Usuario.
    '''
    class Meta:
        model = User
        fields = [
            'username'
        ]
    
    
class BookingSerializer(serializers.ModelSerializer):
    '''
    Serializador de reservas.
    Incluye los datos del departamento y cliente.
    '''
    
    # Agregar datos del usuario relacionado a la reserva
    #user = UserSerializer(read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    
    apartment = serializers.CharField(source='apartment.name', read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'
    