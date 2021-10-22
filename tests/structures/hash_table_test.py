import unittest

from app.exceptions import StructureIsFullError
from app.structures.hash_table import HashTable
from app.store import StoreItem


class TestHashTable(unittest.TestCase):
    def test_is_full(self):
        hash_table = HashTable(2)
        item = StoreItem("apple", 3)
        hash_table.insert(item)
        self.assertFalse(hash_table.is_full())
        hash_table.insert(item)
        self.assertTrue(hash_table.is_full())

    def test_is_empty(self):
        hash_table = HashTable(2)
        self.assertTrue(hash_table.is_empty())
        item = StoreItem("apple", 3)
        hash_table.insert(item)
        self.assertFalse(hash_table.is_empty())

    def test_hashing_produces_correct_hash(self):
        hash_table = HashTable(10)
        self.assertEqual(1, hash_table.simple_hashing('a_key'))
        self.assertEqual(6, hash_table.simple_hashing('b_key'))
        
    def test_double_hashing_produces_correct_hash(self):
        hash_table = HashTable(10)
        self.assertEqual(7, hash_table.double_hashing('a_key'))
        self.assertEqual(3, hash_table.double_hashing('b_key'))

    def test_insert_adds_item_correctly(self):
        hash_table = HashTable(10)
        item = StoreItem("apple", 3)
        hash_table.insert(item)
        expected = [None, None, None, None, None, None, item, None, None, None]
        self.assertEqual(expected, hash_table.data)

    def test_insert_adds_item_correctly_on_collisions(self):
        hash_table = HashTable(10)
        item = StoreItem("apple", 3)
        item_2 = StoreItem("apple", 3)
        item_3 = StoreItem("apple", 3)
        hash_table.insert(item)
        hash_table.insert(item_2)
        hash_table.insert(item_3)
        expected = [None, None, item_2, None, None, None, item, None, item_3, None]
        self.assertEqual(expected, hash_table.data)

    def test_insert_when_full_raises_exception(self):
        hash_table = HashTable(2)
        item = StoreItem("apple", 3)
        item_2 = StoreItem("banana", 3)
        item_3 = StoreItem("orange", 3)
        hash_table.insert(item)
        hash_table.insert(item_2)
        self.assertRaises(StructureIsFullError, hash_table.insert, item_3)

    def test_find_locates_item_correctly_with_collisions(self):
        hash_table = HashTable(5)
        items = [StoreItem("apple", 3), StoreItem("banana", 3), StoreItem("orange", 3), StoreItem("cherry", 3)]
        for i in items:
            hash_table.insert(i)
        self.assertEqual(items[0], hash_table.find_item(items[0].key))
        self.assertEqual(items[1], hash_table.find_item(items[1].key))
        self.assertEqual(items[2], hash_table.find_item(items[2].key))
        self.assertEqual(items[3], hash_table.find_item(items[3].key))

    def test_delete_removes_item(self):
        hash_table = HashTable(5)
        item = StoreItem("apple", 3)
        hash_table.insert(item)
        self.assertFalse(hash_table.is_empty())
        hash_table.delete(item.key)
        self.assertTrue(hash_table.is_empty())


if __name__ == '__main__':
    unittest.main()
