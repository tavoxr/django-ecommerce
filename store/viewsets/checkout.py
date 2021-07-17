from django.shortcuts import render


def checkout(request):
    context={

    }
    return render(request, 'store/Checkout.html', context)