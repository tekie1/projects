from django.db import models

# Create your models here.

from authentication.models import User
from habesha import settings

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2) 
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, null=True, blank=True)
    shipping_method = models.ForeignKey('ShippingMethod', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE
    # ) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}'s Address"
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2) # ISO 3166-1 alpha-2 country cod
class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
class ShippingZone(models.Model):
    name = models.CharField(max_length=100)
    countries = models.ManyToManyField('Country', related_name='shipping_zones')
    regions = models.ManyToManyField('Region', related_name='shipping_zones')

class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    estimated_delivery_time = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    zones = models.ManyToManyField(ShippingZone, related_name='shipping_methods')




        

