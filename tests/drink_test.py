import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennents", 4.95, 2.2)

    def test_has_a_name(self):
        self.assertEqual("Tennents", self.drink.name)

    def test_has_a_price(self):
        self.assertEqual(4.95, self.drink.price)

    def test_has_an_alcohol(self):
        self.assertEqual(2.2, self.drink.alcohol)