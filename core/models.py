from django.db import models

# Create your models here.
class Apartment(models.Model):
    """
    Departamentos disponibles para alquiler en la plataforma.
    """
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"
        ordering = ['city', 'name']

    def __str__(self):
        return f"{self.name} - {self.city}"
    
    
class Availability(models.Model):
    '''
    Disponibilidad de un departamento para alquiler.
    '''
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, 
                                  related_name='availabilities')
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Availability"
        verbose_name_plural = "Availabilities"
        ordering = ['start_date']

    def __str__(self):
        return f"{self.apartment.name} from {self.start_date} to {self.end_date}"
    
    
class Service(models.Model):
    '''
    Servicios disponibles para los departamentos.
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    
class ApartmentService(models.Model):
    """
    Relación entre departamentos y servicios disponibles.
    """
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, 
                                  related_name='apartments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, 
                                related_name='services')

    class Meta:
        verbose_name = "Apartment Service"
        verbose_name_plural = "Apartment Services"
        unique_together = ('apartment', 'service')

    def __str__(self):
        return f"{self.apartment.name} - {self.service.name}"
    
    
class Booking(models.Model):
    """
    Reservas realizadas por los usuarios.
    """
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, 
                                  related_name='bookings_apartment')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, 
                             related_name='bookings_user')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['start_date']

    def __str__(self):
        return f"Booking for {self.apartment.name} by {self.user}"