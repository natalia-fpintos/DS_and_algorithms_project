import logging
from app.exceptions import StructureIsFullError

LOG = logging.getLogger(__name__)


class HashTable:
    def __init__(self, size):
        """Size must be a prime number to prevent infinite loop when probing for insertion"""
        self.data = [None for _ in range(size)]
        self.size = size
        self.count = 0
        self.hashing_base = 255
        self.collisions = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def _numeric_repr(self, key):
        result = 0
        for i, v in enumerate(reversed(key)):
            result += ord(v) * (self.hashing_base ** i)
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

    def find(self, key):
        simple_hash_key = self.simple_hashing(key)
        second_hash_key = self.double_hashing(key)
        i = 0
        index = simple_hash_key
        while self.data[index] is not None:
            if self.data[index].key == key:
                LOG.info(f"Item '{key}' found at index {index}")
                return self.data[index]
            i += 1
            index = (simple_hash_key + (i * second_hash_key)) % self.size
