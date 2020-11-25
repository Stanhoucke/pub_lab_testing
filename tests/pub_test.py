import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):

        self.tennents = Drink("Tennents", 4.95, 2.2)
        self.stella = Drink("Stella", 5.50, 3.5)
        self.fosters = Drink("Fosters", 4.00, 1.5)
        self.carling = Drink("Carling", 4.50, 1.7) 
        self.guiness = Drink("Guiness", 5.95, 2.5)
        self.shiraz = Drink("Shiraz", 7.95, 4.0)
        
        stock = [self.tennents, self.stella, self.fosters, self.carling, self.guiness]
        
        self.pub = Pub("The Prancing Pony", 100.00, stock)

        self.customer_1 = Customer("Dave", 50.00, 56)
        self.customer_2 = Customer("Freddy", 0.50, 21)
        self.customer_3 = Customer("Tommy", 50.00, 17)
        self.customer_4 = Customer("Justin", 0.50, 15)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_money_in_till(self):
        self.assertEqual(100.00, self.pub.till)   

    def test_pub_has_stock(self):
        self.assertEqual(5, len(self.pub.drinks))

    def test_add_money_to_till(self):
        cash = 5.50
        self.pub.add_money_to_till(cash)
        self.assertEqual(105.50, self.pub.till)

    def test_find_drink_by_name(self):
        order_1 = self.tennents.name
        order_2 = self.shiraz.name
        self.assertEqual(self.tennents, self.pub.find_drink_by_name(order_1))
        self.assertEqual(None, self.pub.find_drink_by_name(order_2))

    def test_buy_a_drink(self):
        # Arrange
        customer_1 = self.customer_1
        customer_2 = self.customer_2

        order_1 = self.tennents.name
        order_2 = self.shiraz.name
        # Act
        self.pub.buy_a_drink(customer_1, order_1)
        self.pub.buy_a_drink(customer_2, order_2)

        # Assert

        self.assertEqual(45.05, self.customer_1.wallet)
        self.assertEqual(0.50, self.customer_2.wallet)
        self.assertEqual(104.95, self.pub.till)
