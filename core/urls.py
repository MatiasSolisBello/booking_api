from rest_framework import routers
from django.urls import path, include
from .views import BookingViewset, ServiceViewset, ApartmentViewset

# genera automáticamente las rutas para los ViewSet
router = routers.DefaultRouter()


router.register('services', ServiceViewset)
router.register('apartments', ApartmentViewset)
router.register('bookings', BookingViewset)

urlpatterns = [
    path('', include(router.urls)),
]