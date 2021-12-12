from django.db import models

# Create your models here.


class Pizza(models.Model):
    """This creates a model for pizzas to be stored in the menu database."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return the string representation of the model."""
        return self.name


class Topping(models.Model):
    """This creates a model to store the toppings to each pizza."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """This create a model for the comments to go on each pizza page."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length=80)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
