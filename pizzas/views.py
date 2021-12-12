from django.shortcuts import render, get_object_or_404
from .models import Pizza, Topping
from .forms import CommentForm

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


def pizza_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    comments = pizza.comment_set.order_by("created_on")
    new_comment = None
    # When a comment is posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create a comment object but do not save it to the database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current pizza to the comment
            new_comment.pizza = pizza
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        "pizza": pizza,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }

    return render(request, "pizzas/pizza_comment.html", context)
