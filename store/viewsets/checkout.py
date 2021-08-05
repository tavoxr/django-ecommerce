import json
from store.models import shipping
from django.shortcuts import render
from ..models import Order, ShippingAddress
from django.http import  JsonResponse
import datetime
from ..utils import cookieCart


def checkout(request):

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items =  order.orderitem_set.all()
        cartItems = order.get_total_items
    else:
        cookieData =  cookieCart(request)
        cartItems = cookieData['cartItems']
        order =  cookieData['order']
        items =  cookieData['items']

    context={
        'order': order,
        'items': items,
        'cartItems': cartItems
    }
    return render(request, 'store/Checkout.html', context)



def processOrder(request):
    print(f'data: {request.body}')
    data = json.loads(request.body)

    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete =False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_total_order_ammount):
            order.complete = True
        
        order.save()

        shippingAddress =  ShippingAddress.objects.create(
            customer = customer,
            order =  order,
            address = data['shipping']['address'],
            city =  data['shipping']['city'],
            state =  data['shipping']['state'],
            zipcode =  data['shipping']['zipcode'],

        )

    else:
        print('User is not logged in...')  
    return JsonResponse('Payment complete', safe=False)


