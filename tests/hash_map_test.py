import unittest

from app.hash_map import HashMap
from app.store import StoreItem


class TestHashMap(unittest.TestCase):
    def test_is_full(self):
        hash_map = HashMap(2)
        item = StoreItem("apple", 3)
        hash_map.insert(item)
        self.assertFalse(hash_map.is_full())
        hash_map.insert(item)
        self.assertTrue(hash_map.is_full())

    def test_is_empty(self):
        hash_map = HashMap(2)
        self.assertTrue(hash_map.is_empty())
        item = StoreItem("apple", 3)
        hash_map.insert(item)
        self.assertFalse(hash_map.is_empty())

    def test_hashing(self):
        hash_map = HashMap(1)
        self.assertEqual(1, hash_map.hashing('a_key'))
        self.assertEqual(26, hash_map.hashing('b_key'))

    def test_insert(self):
        hash_map = HashMap(5)
        item = StoreItem("apple", 3)
        hash_map.insert(item)
        expected = [None, item, None, None, None]
        self.assertEqual(expected, hash_map.data)


if __name__ == '__main__':
    unittest.main()
