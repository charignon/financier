"""A stock Grant"""
from bisect import bisect_left, bisect_right
from .component import Component

class StockGrant(Component):
    def __init__(self, amount, schedule):
        self.amount = amount
        self.cliffs_sorted_by_date = [
            (e.date, e.value * amount)
            for e in schedule.vesting_events
        ]
        self.cliffs_dates = [c[0] for c in self.cliffs_sorted_by_date]

    def value(self, start, end):
        # Optimization: narrow down potential range to look at
        ids = bisect_left(self.cliffs_dates, start)
        ide = bisect_right(self.cliffs_dates, end)
        potential_cliffs = self.cliffs_sorted_by_date[ids:ide]

        return sum(amount
                   for date, amount in potential_cliffs
                   if (date >= start and date <= end))
