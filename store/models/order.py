from django.db import models
from ..models import Customer, Product


class Order(models.Model):
    customer= models.ForeignKey(Customer, null=True, blank=True, on_delete= models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f'Order:{self.id} - {self.customer.name}'

    #@property
    #def get_total_order_ammount(self):
    #   orderitems = self.orderitem_set.all()
    #   total = for item in orderitems


class OrderItem(models.Model):
   product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
   order =  models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
   quantity = models.IntegerField(default=0, null= True, blank=True )
   date_created  = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f'id: {self.id} - order {self.order.id} / {self.product.name} - {self.quantity} items'

   @property 
   def get_total_ammount(self):
    
        total =  self.quantity * self.product.price
        return total
