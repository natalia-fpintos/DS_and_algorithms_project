import unittest

from app.exceptions import StructureIsFullError
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

    def test_hashing_produces_correct_hash(self):
        hash_map = HashMap(10)
        self.assertEqual(1, hash_map.simple_hashing('a_key'))
        self.assertEqual(6, hash_map.simple_hashing('b_key'))
        
    def test_double_hashing_produces_correct_hash(self):
        hash_map = HashMap(10)
        self.assertEqual(7, hash_map.double_hashing('a_key'))
        self.assertEqual(3, hash_map.double_hashing('b_key'))

    def test_insert_adds_item_correctly(self):
        hash_map = HashMap(10)
        item = StoreItem("apple", 3)
        hash_map.insert(item)
        expected = [None, None, None, None, None, None, item, None, None, None]
        self.assertEqual(expected, hash_map.data)

    def test_insert_adds_item_correctly_on_collisions(self):
        hash_map = HashMap(10)
        item = StoreItem("apple", 3)
        item_2 = StoreItem("apple", 3)
        item_3 = StoreItem("apple", 3)
        hash_map.insert(item)
        hash_map.insert(item_2)
        hash_map.insert(item_3)
        expected = [None, None, item_2, None, None, None, item, None, item_3, None]
        self.assertEqual(expected, hash_map.data)

    def test_insert_when_full_raises_exception(self):
        hash_map = HashMap(2)
        item = StoreItem("apple", 3)
        item_2 = StoreItem("banana", 3)
        item_3 = StoreItem("orange", 3)
        hash_map.insert(item)
        hash_map.insert(item_2)
        self.assertRaises(StructureIsFullError, hash_map.insert, item_3)


if __name__ == '__main__':
    unittest.main()
