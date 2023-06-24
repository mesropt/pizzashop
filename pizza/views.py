from django.shortcuts import render, redirect, get_object_or_404
from pizza.forms import PizzaForm
from pizza.models import Pizza


def list_pizza(request):
    return render(request, 'pizza/pizza_list.html')

def add_pizza(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home:home')
    return render(request, 'pizza/add_pizza.html', context={'form': form})

def update_pizza(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    return render(request, 'pizza/update.html', {'form': form})


def delete_pizza(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        pizza.delete()
        return redirect('home:home')
    return render(request, 'pizza/delete.html', {'pk': pizza.pk})

def pizza_detail(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    return render(request, 'pizza/detail.html', {'pizza': pizza})
