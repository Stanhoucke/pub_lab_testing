import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Dave", 50.00, 56)
        self.customer_2 = Customer("Freddy", 0.50, 21)
        self.customer_3 = Customer("Tommy", 50.00, 17)
        self.customer_4 = Customer("Justin", 0.50, 15)

        self.tennents = Drink("Tennents", 4.95, 2.2)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer_1.name)

    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer_1.wallet)

    def test_customer_can_afford(self):
        can_afford = self.customer_1.can_afford(self.tennents)
        cant_afford = self.customer_2.can_afford(self.tennents)
        self.assertEqual(True, can_afford)
        self.assertEqual(False, cant_afford)

    def test_remove_from_wallet(self):
        price_of_item = 5.00
        self.customer_1.remove_money_from_wallet(price_of_item)
        self.assertEqual(45.00, self.customer_1.wallet)

    def test_customer_has_age(self):
        self.assertEqual(17, self.customer_3.age)

    def test_customer_starts_sober(self):
        self.assertEqual(0, self.customer_3.drunkeness)