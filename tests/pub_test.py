import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        stock = [
            "Tennents",
            "Stella",
            "Fosters",
            "Carling",
            "Guiness"
        ]
        self.pub = Pub("The Prancing Pony", 100.00, stock)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_money_in_till(self):
        self.assertEqual(100.00, self.pub.till)   

    def test_pub_has_stock(self):
        self.assertEqual(5, len(self.pub.drinks))


