from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    @action(detail=False, url_path='user/(?P<user_id>[^/.]+)')
    def by_user(self, request, user_id=None):
        bookings = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)
    

    
