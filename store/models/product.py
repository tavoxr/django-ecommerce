from django.db import models


class Product(models.Model):
    name =  models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(default="productDefaultImg1.jpg",  null=True, blank=True)

    def __str__(self):
        return self.name
