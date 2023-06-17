from django.shortcuts import render
from pizza.models import Pizza
# Create your views here.


def home(request):
    pizza_list = Pizza.objects.all()
    return render(request, 'home/index.html', {'pizza_list': pizza_list})
