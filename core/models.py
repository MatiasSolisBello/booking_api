from django.db import models

# Create your models here.
class Apartment(models.Model):
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
    
    
