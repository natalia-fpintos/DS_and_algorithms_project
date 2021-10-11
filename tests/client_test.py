import unittest

from app.client import Client, CartItem
from app.store import Store


class CartItemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cart_item = CartItem('a', 5)

    def test_increment_item_quantity(self):
        self.cart_item.increment_quantity_by(2)
        self.assertEqual(7, self.cart_item.quantity)

    def test_decrease_item_quantity(self):
        self.cart_item.decrease_quantity_by(3)
        self.assertEqual(2, self.cart_item.quantity)


class ClientTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client(Store('./store.txt', 5))
        self.cart_item = CartItem('a', 5)

    def test_client_can_add_item_to_cart(self):
        self.client.add_item_to_cart('a')
        self.assertEqual(4, self.client.store.find_item('a').stock)
        self.assertEqual(1, self.client.cart.find('a').quantity)


if __name__ == '__main__':
    unittest.main()