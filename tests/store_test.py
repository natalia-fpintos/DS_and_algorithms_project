import unittest

from app.store import Store


class StoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.store = Store('./store.txt', 5)

    def test_store_init(self):
        expected_items = ['c', 'd', 'e', 'b', 'a']
        self.assertEqual(expected_items, self.store.items)
        self.assertEqual(5, self.store.items_table.size)
        self.assertTrue(self.store.items_table.is_full())

    def test_update_stock(self):
        self.store.update_stock('c', 1)
        self.assertEqual(3, self.store.find_item('c').stock)


if __name__ == '__main__':
    unittest.main()
