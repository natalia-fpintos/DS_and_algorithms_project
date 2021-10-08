class HashMap:
    def __init__(self, size):
        self.data = [None for _ in range(size)]
        self.size = size
        self.count = 0
        self.hashing_base = 255

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def hashing(self, key):
        result = 0
        for i, v in enumerate(reversed(key)):
            result += ord(v) * (self.hashing_base ** i)
        return result % self.size

    def insert(self, item):
        hash_key = self.hashing(item.key)
        while self.data[hash_key] is not None:
            print(f"Collision inserting at key {hash_key}")
            hash_key += 1
            hash_key %= self.size

        self.data[hash_key] = item
        self.count += 1
