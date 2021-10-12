from app.structures.hash_table import HashTable

from app.structures.trie import Trie


class StoreItem:
    def __init__(self, name, stock):
        self.key = name
        self.name = name
        self.stock = stock


class Store:
    def __init__(self, store_location, size):
        self.items = self._get_store_items(store_location)
        self.items_table = HashTable(size)
        self.items_dictionary = Trie()

        self._init_items_table()
        self._init_items_dictionary()

    def _get_store_items(self, filename):
        with open(filename) as f:
            return f.read().splitlines()

    def _init_items_table(self):
        for i in self.items:
            self.items_table.insert(StoreItem(i, 5))

    def _init_items_dictionary(self):
        for i in self.items:
            self.items_dictionary.insert(i)

    def find_item(self, key):
        return self.items_table.find_item(key)

    def add_stock(self, item_key, quantity):
        item = self.items_table.find_item(item_key)
        if item:
            item.stock += quantity
        return item is not None

    def remove_stock(self, item_key, quantity):
        item = self.items_table.find_item(item_key)
        if item and item.stock >= quantity:
            item.stock -= quantity
            return True
        return False
