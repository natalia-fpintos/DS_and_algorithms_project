import logging
from app.structures.hash_table import HashTable

LOG = logging.getLogger(__name__)


class CartItem:
    def __init__(self, name, quantity):
        self.key = name
        self.name = name
        self.quantity = quantity

    def increment_quantity_by(self, quantity):
        self.quantity += quantity

    def decrease_quantity_by(self, quantity):
        self.quantity -= quantity


class Client:
    instances = 0

    def __init__(self, store):
        self.instances += 1
        self.id = self.instances
        self.cart = HashTable(47)
        self.store = store

    def add_item_to_cart(self, item_key, quantity=1):
        if self.store.remove_stock(item_key, quantity):
            self.cart.insert(CartItem(item_key, quantity))
            print("Item(s) added to the cart")
        else:
            print("There is not enough stock for this item")

    def remove_item_from_cart(self, item_key):
        cart_item = self.cart.find_item(item_key)
        if not cart_item:
            LOG.error(f'Could not find item {cart_item} in the cart')
            return

        if self.store.add_stock(item_key, cart_item.quantity):
            self.cart.delete(item_key)

    def select_options(self):
        selecting = True
        while selecting:
            print("\n### Please select one of the following options:\n\t1. Store item search"
                  "\n\t2. Item search suggestion\n\t3. View/edit cart items\n\t4. Exit store")
            option_selected = input("Type your option here: ")

            if option_selected == '1':
                self.store_item_search()
            elif option_selected == '2':
                self.suggest_item()
            elif option_selected == '3':
                pass
            elif option_selected == '4':
                print("\n~~~ Thanks for your visit! ~~~")
                selecting = False
            else:
                print("Invalid option\n")

    def store_item_search(self):
        print("\n### Store item search")
        while True:
            item_searched = input(
                "Type an item name (i.e. strawberries, cherries, bananas) or type QUIT to exit the search: ")

            if item_searched == 'QUIT':
                break

            found = self.store.find_item(item_searched)

            if found:
                found.display()
                self.prompt_add_to_cart(found.name)
            else:
                print(f"Item {item_searched} was not found")

    def suggest_item(self):
        print("\n### Item search suggestion")
        while True:
            search_term = input(
                "Type the first character(s) for your search to see an item suggestion "
                "(i.e. 'ap', 'c') or type QUIT to exit the search: ")

            if search_term == 'QUIT':
                break

            suggestion = self.store.get_suggestion(search_term)

            if suggestion:
                suggestion.display()
                self.prompt_add_to_cart(suggestion.name)
            else:
                print(f"Could not find a match for '{search_term}'")

    def prompt_add_to_cart(self, item):
        add_item = input(f"Would you like to add '{item}' to the cart? (y/n): ")
        while add_item not in ['y', 'n']:
            add_item = input(f"Would you like to add '{item}' to the cart? (y/n): ")

        if add_item == 'y':
            quantity = input("Please enter amount to add to the cart (max 5): ")
            try:
                quantity = int(quantity)
            except ValueError:
                print("Please enter a valid amount")
                return

            if quantity not in list(range(1, 6)):
                print("Please enter a valid amount")
                return

            self.add_item_to_cart(item, int(quantity))
        else:
            print("Item will not be added to the cart")

    def view_edit_cart(self):
        print("\n### View/edit cart items")
        while True:
            action = input(" or type QUIT to exit the cart: ")

            if action == 'QUIT':
                break
