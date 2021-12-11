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
