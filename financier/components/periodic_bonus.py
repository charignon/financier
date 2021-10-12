from bisect import bisect_left, bisect_right
from .component import Component


class PeriodicBonus(Component):
    def __init__(self, amount, date_seq, **kwargs):
        Component.__init__(self, **kwargs)
        self.amount = amount
        self.date_seq = sorted(date_seq)

    def value(self, start, end):
        ids = bisect_left(self.date_seq, start)
        ide = bisect_right(self.date_seq, end)
        potential_bonuses = self.date_seq[ids:ide]

        return sum(self.amount
                   for date in potential_bonuses
                   if (date >= start and date <= end))
