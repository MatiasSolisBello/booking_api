from .models import ApartmentImages, Booking, Service, Apartment, ApartmentService
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

class ApartmentImagesSerializer(serializers.ModelSerializer):
    '''
    Serializador de las imágenes de los departamentos.
    '''
    image = serializers.ImageField(read_only=True)
    class Meta:
        model = ApartmentImages
        fields = ["apartment", "image"]     
        
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
    #services = ApartmentServiceSerializer(source='apartments', many=True)
    
    images = ApartmentImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, 
                                       allow_empty_file = False, 
                                       use_url = False
                                    ),write_only=True)
    
    class Meta:
        model = Apartment
        fields = [
            'name',
            'city',
            'address',
            'price',
            'bedrooms',
            'bathrooms',
            'description',
            'images',
            'uploaded_images'
        ]
        
    def create(self, validated_data):
        print(validated_data)
        uploaded_images = validated_data.pop("uploaded_images")
        apartment = Apartment.objects.create(**validated_data)
        print('----------------')
        print('apartment: ', apartment)
        print('uploaded_images: ', uploaded_images)
        print('----------------')
        for image in uploaded_images:
            new_image = ApartmentImages.objects.create(apartment=apartment, 
                                                       image=image)
        return apartment
        

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializador de Usuario.
    '''
    class Meta:
        model = User
        fields = [
            'username', 'email'
        ]
    
    
class BookingSerializer(serializers.ModelSerializer):
    '''
    Serializador de reservas.
    Incluye los datos del departamento y cliente.
    '''
    
    user = UserSerializer(read_only=True)
    #user = serializers.CharField(source='user.username', read_only=True)
    
    #apartment = ApartmentSerializer(read_only=True)
    apartment = serializers.CharField(source='apartment.name', read_only=True)
    
    #services = serializers.SerializerMethodField()
    
    class Meta:
        model = Booking
        fields = '__all__'
        
    #def get_services(self, obj):
    #    services = Service.objects.filter(services__apartment=obj.apartment)
    #    return ServiceSerializer(services, many=True).data
    