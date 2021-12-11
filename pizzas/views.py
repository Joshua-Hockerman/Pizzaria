from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.


def index(request):
    """The home page for the Pizzas app"""
    return render(request, "pizzas/index.html")


def menu(request):
    """Show all the pizzas on the menu"""
    items = Pizza.objects.order_by("name")
    context = {"items": items}
    return render(request, "pizzas/menu.html", context)


def toppings(request, pizza_id):
    """Show a single pizza and all of its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("name")
    context = {"pizza": pizza, "toppings": toppings}

    return render(request, "pizzas/toppings.html", context)
