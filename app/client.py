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
                self.store.store_item_search()
            elif option_selected == '2':
                self.search_item()
            elif option_selected == '3':
                pass
            elif option_selected == '4':
                print("\n~~~ Thanks for your visit! ~~~")
                selecting = False
            else:
                print("Invalid option\n")

    def search_item(self):
        print("\n### Item search suggestion")
        while True:
            search_term = input(
                "Type the first character(s) for your search to see an item suggestion "
                "(i.e. 'ap', 'c') or type QUIT to exit the search: ")

            if search_term == 'QUIT':
                break

            suggestion = self.store.autocomplete(search_term)

            if suggestion:
                print(f"Item suggestion: {suggestion}")
            else:
                print(f"Could not find a match for '{search_term}'")
