import logging
from app.exceptions import StructureIsFullError

LOG = logging.getLogger(__name__)


class HashTable:
    HASHING_BASE = 255

    def __init__(self, size):
        """Size must be a prime number to prevent infinite loop when probing for insertion"""
        self.data = [None for _ in range(size)]
        self.size = size
        self.count = 0
        self.collisions = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def _numeric_repr(self, key):
        result = 0
        for i, v in enumerate(reversed(key)):
            result += ord(v) * (self.HASHING_BASE ** i)
        return result

    def simple_hashing(self, key):
        return self._numeric_repr(key) % self.size

    def double_hashing(self, key):
        prime = 7 if self.size > 7 else 1
        return prime - (self._numeric_repr(key) % prime)

    def insert(self, item):
        if self.is_full():
            raise StructureIsFullError(HashTable.__name__)

        simple_hash_key = self.simple_hashing(item.key)
        second_hash_key = self.double_hashing(item.key)
        i = 0
        index = simple_hash_key
        while self.data[index] is not None:
            LOG.debug(f"Collision for '{item.key}' inserting at index {index}")
            self.collisions += 1
            i += 1
            index = (simple_hash_key + (i * second_hash_key)) % self.size

        self.data[index] = item
        self.count += 1

    def _find_index(self, key):
        if key is not None:
            simple_hash_key = self.simple_hashing(key)
            second_hash_key = self.double_hashing(key)
            i = 0
            index = simple_hash_key
            while self.data[index] is not None:
                if self.data[index].key == key:
                    LOG.debug(f"Item '{key}' found at index {index}")
                    return index
                i += 1
                index = (simple_hash_key + (i * second_hash_key)) % self.size

    def find_item(self, key):
        index = self._find_index(key)
        return self.data[index] if index is not None else None

    def delete(self, key):
        index = self._find_index(key)
        if index:
            self.data[index] = None
            self.count -= 1
        else:
            print("Not found")

    def display_all(self):
        if self.is_empty():
            print("Empty")
        for i in self.data:
            if i:
                i.display()
