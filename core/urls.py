from rest_framework import routers
from django.urls import path, include
from .views import ServiceViewset, ApartmentViewset

router = routers.DefaultRouter()
router.register('services', ServiceViewset)
router.register('apartments', ApartmentViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]