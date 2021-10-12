from .component import Component


class OneTimeBonus(Component):
    def __init__(self, amount, payoff_date, **kwargs):
        Component.__init__(self, **kwargs)
        self.amount = amount
        self.payoff_date = payoff_date

    def value(self, start, end):
        if self.payoff_date >= start and self.payoff_date <= end:
            return self.amount
        return 0
