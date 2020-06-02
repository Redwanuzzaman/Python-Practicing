class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        tot_cents = self.cents + deposit_cents
        extra_dollars = tot_cents // 100
        self.cents = tot_cents % 100
        self.dollars += deposit_dollars + extra_dollars

