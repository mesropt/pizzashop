from django.shortcuts import render

# Create your views here.


def list_pizza(request):
    return render(request, 'pizza/pizza_list.html')
