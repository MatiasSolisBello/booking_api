from django.contrib.auth import get_user_model 
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from core.models import Apartment


User = get_user_model()

# Create your tests here.
class TestApartmentAPI(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', 
                                                        email='admin@example.com',
                                                        password='adminpass')
        self.normal_user = User.objects.create_user(username='user',
                                                    email='user@example.com', 
                                                    password='userpass')
        
        self.apartment = Apartment.objects.create(
            name='Test Apartment',
            city='Test City',
            address='123 Test St',
            price=100,
            bedrooms=2,
            bathrooms=1,
            description='A nice place to stay.'
        )
        self.url = reverse('apartment-detail', 
                           kwargs={'apartment_id': self.apartment.pk})
        
    def test_get_apartment(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.apartment.name)

    def test_unauthorized_update_apartment(self):
        data = {"name": "Updated Apartment"}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_delete_apartment(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_only_admins_can_delete_product(self):
        # test normal user
        self.client.login(username='user', password='userpass')
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Apartment.objects.filter(pk=self.apartment.pk).exists())

        # test admin user
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Apartment.objects.filter(pk=self.apartment.pk).exists())
        