from django.urls import path, include
from .viewsets import *

urlpatterns=[
    path('', store, name='store' ),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_cart, name='update_item' )
]