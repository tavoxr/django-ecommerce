from django.shortcuts import render



def cart(request):
    context = {

    }
    return render(request,'store/Cart.html', context)



