class Pub():
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_money_to_till(self, cash):
        self.till += cash

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def buy_a_drink(self, customer, drink_name):
        if self.find_drink_by_name(drink_name) != None:
            order = self.find_drink_by_name(drink_name)
            if customer.can_afford(order) == True:
                customer.remove_money_from_wallet(order.price)
                self.add_money_to_till(order.price)
