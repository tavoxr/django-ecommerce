import json
from .models import *

def cookieCart(request):

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart', cart)
    items = []
    order = {'get_total_order_ammount': 0, 'get_total_items': 0}
    cartItems = order['get_total_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id = i)
            total = (product.price * cart[i]['quantity'])

            order['get_total_order_ammount'] += total
            order['get_total_items'] += cart[i]['quantity']

            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image': product.image,
                },
                'quantity': cart[i]['quantity'],
                'get_total_ammount': total,
            }

            items.append(item)
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items }



def cartData(request):
   
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


    return {'cartItems': cartItems, 'order': order, 'items': items}