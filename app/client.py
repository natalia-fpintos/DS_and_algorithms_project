import logging
from app.hash_table import HashTable


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
        found = self.store.find_item(item_key)
        if not found:
            LOG.error(f'Could not find item {item_key} in the store')
            return

        if found.stock >= quantity:
            self.store.update_stock(item_key, found.stock - quantity)
            self.cart.insert(CartItem(found.name, quantity))

    def remove_item_from_cart(self, item):
        pass

    def increment_quantity(self, item, quantity):
        pass

    def decrease_quantity(self, item, quantity):
        pass

    def search_item(self, search_term):
        pass

    def checkout(self):
        pass
