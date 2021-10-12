from .component import Component

class DailyReward(Component):
    """A component that represents a daily reward, like a Salary"""
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

    def pay_per_day(self):
        return float(self.yearly_amount) / 365

    def value(self, start, end):
        days = (end - start).days + 1
        return days * self.pay_per_day()
