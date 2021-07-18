from django.db import models
from django.db.models.deletion import SET_NULL
from ..models import Customer, Order


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete= models.SET_NULL)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    state =  models.CharField(max_length=200, null=True)
    zipcode =  models.CharField(max_length=200, null=True)
    date_added =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

