from django.db import models

# Create your models here.


class Pizza(models.Model):
    """This creates a model for pizzas to be stored in the menu database."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return the string representation of the model."""
        return self.name


class Topping(models.Model):
    """Thie creates a model to store the toppings to each pizza."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
