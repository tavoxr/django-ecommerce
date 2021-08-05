import json
from store.models.order import OrderItem
from store.models.product import Product
from store.models.users import Customer
from store.models import shipping
from django.shortcuts import render
from ..models import Order, ShippingAddress
from django.http import  JsonResponse
import datetime
from ..utils import cookieCart ,cartData


def checkout(request):

    data =  cartData(request)
    
    cartItems =  data['cartItems']
    order  = data['order']
    items = data['items']

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
        print('COOKIES', request.COOKIES)
        
        name = data['form']['name']
        email =  data['form']['email']

        cookieData =  cookieCart(request)
        items = cookieData['items']

        customer, created = Customer.objects.get_or_create( 
            email = email
            )
        
        customer.name = name
        customer.save()
        
        order =  Order.objects.create(
            customer =  customer,
            complete = False
        )

        for item in items:
            product = Product.objects.get(id= item['product']['id'])

            orderItem = OrderItem.objects.create(
                product = product,
                order = order,
                quantity = item['quantity']
            )



    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_total_order_ammount):
        order.complete = True
        
    order.save()


    return JsonResponse('Payment complete', safe=False)


