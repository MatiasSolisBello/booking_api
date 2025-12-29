from .models import ApartmentImages, Booking, Service, Apartment, ApartmentService
from django.contrib.auth.models import User
from django.db.models import Q
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
    icon = serializers.CharField(source='service.icon')

    class Meta:
        model = ApartmentService
        fields = ['name', 'price', 'icon']
     
class ApartmentSerializer(serializers.ModelSerializer):
    '''
    Serializador de Departamento.
    Incluye los servicios disponibles para el departamento.
    '''
    
    # Agregar datos del servicio relacionado al departamento
    services = ApartmentServiceSerializer(source='apartments', many=True)
    
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
            'uploaded_images',
            'services'
        ]
        
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        apartment = Apartment.objects.create(**validated_data)
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
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.all()
    )
    apartment_id = serializers.PrimaryKeyRelatedField(
        source='apartment',
        queryset=Apartment.objects.all()
    )
    
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
    
    def create(self, validated_data):
        apartment = validated_data['apartment']
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']
        
        # Buscar reservas que se solapan con el rango solicitado
        check_avaibility = Booking.objects.filter(apartment=apartment).filter(
            Q(start_date__lt=end_date) & Q(end_date__gt=start_date)
        )

        if check_avaibility:
            start_date=start_date.strftime("%d/%m/%Y")
            end_date=end_date.strftime("%d/%m/%Y")
            raise serializers.ValidationError(
                f"El departamento no está disponible entre {start_date} al {end_date}")
        else:
            booking = Booking.objects.create(**validated_data)
            return booking
    