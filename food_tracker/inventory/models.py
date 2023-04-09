from django.db import models


# Represents individual ingrediant's
class Ingredient(models.Model):
    name = models.CharField(max_length=20, unique=True)
    quantity = models.FloatField(max_length=10, default=0)
    unit = models.CharField(max_length=10)
    price_per_unit = models.FloatField(max_length=5, default=0)

    def __str__(self):
        return f"{self.name}: {self.quantity}"


# Represents restaurant's menu
class MenuItem(models.Model):
    title = models.CharField(max_length=40, unique=True)
    price = models.FloatField(max_length=5)

    def __str__(self):
        return f"{self.title}, price: {self.price}"


# Represents individual menu item recipie
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.menu_item} recipe"


# Represents purchases and time of the purchase of the menu
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item} purchased at: {self.timestamp}"
