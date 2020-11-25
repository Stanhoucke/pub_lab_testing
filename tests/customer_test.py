import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Dave", 50.00)
        self.customer_2 = Customer("Freddy", 0.50)

        self.tennents = Drink("Tennents", 4.95)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer_1.name)

    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer_1.wallet)

    def test_customer_can_afford(self):
        can_afford = self.customer_1.can_afford(self.tennents)
        cant_afford = self.customer_2.can_afford(self.tennents)
        self.assertEqual(True, can_afford)
        self.assertEqual(False, cant_afford)
