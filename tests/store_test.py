import unittest

from app.store import Store


class StoreTest(unittest.TestCase):
    def test_store_init(self):
        store = Store('./store.txt', 5)
        expected_items = ['c', 'd', 'e', 'b', 'a']
        self.assertEqual(expected_items, store.items)
        self.assertEqual(5, store.items_map.size)
        self.assertTrue(store.items_map.is_full())


if __name__ == '__main__':
    unittest.main()
