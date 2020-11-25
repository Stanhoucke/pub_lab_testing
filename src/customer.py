class Customer():

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def can_afford(self, drink):
        return self.wallet >= drink.price

    def remove_money_from_wallet(self, cash):
        self.wallet -= cash