from django.shortcuts import render
from pizza.models import Pizza
from django.core.paginator import Paginator


def home(request):
    query = request.GET.get('q')
    if query:
        pizza_list = Pizza.objects.filter(name__icontains=query)
    else:
        pizza_list = Pizza.objects.all()
    pizza_list = pizza_list.order_by('-pk')
    paginator = Paginator(pizza_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "home/index.html", {"pizza_list": page_obj})
