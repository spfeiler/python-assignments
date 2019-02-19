user_input = ''
stores = []

from grocery_list_classes import *

def shopping_list_menu():
    print('Press 1 to create a new shopping list: ')
    print('Press 2 to add items to existing shopping lists: ')
    print('Press 3 to view shopping lists: ')
    print('Press q to quit: ')

def add_list():
    store_name = input('Enter store name: ')
    store = ShoppingList(store_name)
    stores.append(store)

def view_stores():
    for store in stores:
        print(f"{stores.index(store)+1} - {store.name}")

def add_item():
    while True:
        try:
            view_stores()
            choose_index = int(input('Enter an index from the list above to add an item to that store: '))
            store_index = stores[choose_index - 1]
            name = input('Enter item name: ')
            price = float(input('Enter item price: '))
            quantity = int(input('Enter item quantity: '))
            item = GroceryItem(name, price, quantity)
            store_index.grocery_items.append(item)
            break
        except:
            print('Oops! Something went wrong. Please try again.')

def list_total():
    total = 0
    for index in range(0,len(stores)):
        store = stores[index]
        for grocery_item in store.grocery_items:
            total += (grocery_item.price * grocery_item.quantity)
            print(total)

def view_lists():
    for index in range(0,len(stores)):
        store = stores[index]
        print(f"{store.name}:")
        for grocery_item in store.grocery_items:
            print(f"{grocery_item.name} - ${grocery_item.price} - {grocery_item.quantity}")
    list_total()

while user_input != 'q':
    shopping_list_menu()
    user_input = input('Select menu option (1, 2, 3, q): ')
    if user_input == '1':
        add_list()
    elif user_input == '2':
        add_item()
    elif user_input == '3':
        view_lists()
