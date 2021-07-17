from django.shortcuts import render


def store(request):
    context = {

    }
    return render(request, 'store/Store.html', context)
