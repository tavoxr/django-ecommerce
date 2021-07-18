from django.shortcuts import render
from ..models import Product

def store(request):
    products = Product.objects.all()


    context = {
        'products': products

    }
    return render(request, 'store/Store.html', context)
