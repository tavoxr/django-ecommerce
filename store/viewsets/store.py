from django.shortcuts import render
from ..models import Product, Order
from ..utils import cookieCart

def store(request):

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items =  order.orderitem_set.all()
        cartItems = order.get_total_items
    else:
        cookieData =  cookieCart(request)
        cartItems = cookieData['cartItems']
        



    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems

    }
    return render(request, 'store/Store.html', context)
