from app.hash_table import HashTable


class Client:
    instances = 0

    def __init__(self):
        self.instances += 1
        self.id = self.instances
        self.cart = HashTable(47)

    def add_item_to_cart(self, item):
        pass

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
