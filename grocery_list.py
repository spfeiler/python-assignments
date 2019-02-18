stores = []

class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.grocery_items = []

    def __repr__(self):
        return self.name

class GroceryItem:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

def shopping_list_menu():
    print('Press 1 to create a new shopping list: ')
    print('Press 2 to add items to existing shopping list(s): ')
    print('Press 3 to view shopping list(s): ')
    print('Press q to quit: ')

def add_list():
    store_name = input('Enter store name: ')
    store = ShoppingList(store_name)
    stores.append(store)

def view_stores():
    for store in stores:
        print(f"{store.name}")

def add_item():
    view_stores()
    choose_list = input('Enter store from the list above to add an item: ')
    item_name = input('Enter item name: ')
    item = GroceryItem(item_name)

    for store in stores:
        if store.name == choose_list:
            store.grocery_items.append(item)

def view_lists():
    for store in stores:
        print(f"{store.name}:")
        for item in store: #<-- returns TypeError: 'ShoppingList' object is not iterable. Not sure why.
            print(f"-{item.name}")

user_input = ''

while user_input != 'q':
    shopping_list_menu()
    user_input = input('Select menu option (1, 2, 3, q): ')
    if user_input == '1':
        add_list()
    elif user_input == '2':
        add_item()
    elif user_input == '3':
        view_lists()
