import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):

        self.tennents = Drink("Tennents", 4.95)
        self.stella = Drink("Stella", 5.50)
        self.fosters = Drink("Fosters", 4.00)
        self.carling = Drink("Carling", 4.50) 
        self.guiness = Drink("Guiness", 5.95)
        
        stock = [self.tennents, self.stella, self.fosters, self.carling, self.guiness]
        
        self.pub = Pub("The Prancing Pony", 100.00, stock)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_money_in_till(self):
        self.assertEqual(100.00, self.pub.till)   

    def test_pub_has_stock(self):
        self.assertEqual(5, len(self.pub.drinks))


