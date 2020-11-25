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

    def check_age(self, customer):
        return customer.age >= 18

    def check_drunkeness(self, customer):
        return customer.drunkeness > 10

    def buy_a_drink(self, customer, drink_name):
        if self.check_age(customer) == True and self.check_drunkeness(customer) == False:
            if self.find_drink_by_name(drink_name) != None:
                order = self.find_drink_by_name(drink_name)
                if customer.can_afford(order) == True:
                    customer.remove_money_from_wallet(order.price)
                    self.add_money_to_till(order.price)
                    customer.increase_customer_drunkeness(order)