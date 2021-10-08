from app.hash_map import HashMap


class StoreItem:
    def __init__(self, name, stock):
        self.key = name
        self.name = name
        self.stock = stock


class Store:
    def __init__(self, store_location, size):
        self.items = self._get_store_items(store_location)
        self.items_map = HashMap(size)

        self._init_items_map()

    def _get_store_items(self, filename):
        with open(filename) as f:
            return f.read().splitlines()

    def _init_items_map(self):
        for i in self.items:
            self.items_map.insert(StoreItem(i, 5))
