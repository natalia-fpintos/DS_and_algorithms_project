from app.hash_table import HashTable


class StoreItem:
    def __init__(self, name, stock):
        self.key = name
        self.name = name
        self.stock = stock


class Store:
    def __init__(self, store_location, size):
        self.items = self._get_store_items(store_location)
        self.items_table = HashTable(size)

        self._init_items_table()

    def _get_store_items(self, filename):
        with open(filename) as f:
            return f.read().splitlines()

    def _init_items_table(self):
        for i in self.items:
            self.items_table.insert(StoreItem(i, 5))
