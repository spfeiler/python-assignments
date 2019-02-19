class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.grocery_items = []

    def list_total(self, a, b):
        total = 0
        total += (a * b)
        return total

class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
