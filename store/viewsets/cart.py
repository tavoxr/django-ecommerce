from django.shortcuts import render
from ..models import Order, OrderItem, Customer


def cart(request):
    
    if request.user.is_authenticated:
        customer =  request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete= False)
        items = order.orderitem_set.all()
        totalItems = items.count()
        
    else:
        items = []


    context = { 'items': items, 
                'totalItems': totalItems,
                
                 }
    return render(request,'store/Cart.html', context)



