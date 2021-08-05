from django.shortcuts import render
from ..models import Product, Order
from ..utils import cookieCart, cartData

def store(request):

    data = cartData(request)

    cartItems =  data['cartItems']

    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems

    }
    
    return render(request, 'store/Store.html', context)
