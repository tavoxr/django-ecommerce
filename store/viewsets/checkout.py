from django.shortcuts import render
from ..models import Order

def checkout(request):

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items =  order.orderitem_set.all()
        cartItems = order.get_total_items
    else:
        items= []
        order = {'get_total_order_ammount': 0, 'get_total_items': 0}
        cartItems = order['get_total_items']


    context={
        'order': order,
        'items': items,
        'cartItems': cartItems
    }
    return render(request, 'store/Checkout.html', context)