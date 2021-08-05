import json
from store.models import product
from store.models.product import Product
from django.shortcuts import render
from ..models import Order, OrderItem, Customer
from django.http import JsonResponse
from ..utils  import cartData

def cart(request):
    
    data = cartData(request)
    
    cartItems = data['cartItems']
    order =  data['order']
    items = data['items']
        
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
