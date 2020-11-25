class Customer():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0.0

    def can_afford(self, drink):
        return self.wallet >= drink.price

    def remove_money_from_wallet(self, cash):
        self.wallet -= cash
        self.wallet = round(self.wallet, 2)

    def increase_customer_drunkeness(self, drink):
        self.drunkeness += drink.alcohol