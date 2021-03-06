"""Defines the url patterns for pizzas."""

from django.urls import path

from . import views

app_name = "pizzas"

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("menu/<int:pizza_id>/", views.toppings, name="toppings"),
    path("toppings/<int:pizza_id>/", views.pizza_comment, name="pizza_comment"),
]
