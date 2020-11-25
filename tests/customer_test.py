import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer.wallet)
