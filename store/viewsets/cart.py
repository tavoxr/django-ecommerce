import json
from store.models.product import Product
from django.shortcuts import render
from ..models import Order, OrderItem, Customer
from django.http import JsonResponse

def cart(request):
    
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_items
        
    else:
        items = []
        order = {'get_total_order_ammount': 0, 'get_total_items': 0}
        cartItems = order['get_total_items']


    context = { 'items': items, 
                'order': order,
                'cartItems': cartItems
                
                 }
    return render(request,'store/Cart.html', context)



def update_cart(request):
    data = json.loads(request.body)
    print('req.body', request.body)
    productId = data['productId']
    action = data['action']
    print(f'productId: {productId},  action: {action}')


    customer = request.user.customer
    product = Product.objects.get(id =  productId)
    order, created = Order.objects.get_or_create(customer = customer,
                                                 complete = False
                                                )

    orderItem, created = OrderItem.objects.get_or_create(order = order,
                                                         product = product                                                      
                                                        )

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
