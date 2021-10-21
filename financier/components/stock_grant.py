"""A stock Grant"""
from bisect import bisect_left, bisect_right
from .component import Component
from .stock import Stock

# TODO variable stock value
# TODO stripe type grant
class StockGrant(Component):
    def __init__(self, amount, schedule, stock=None, stock_value_date=None):
        if stock is None:
            self.stock = Stock(
                initial_value = 1,
                yearly_multiplier = 1,
            )
        else:
            self.stock = stock
        if stock_value_date is None:
            self.stock_value_date = self.stock.initial_value_date
        else:
            self.stock_value_date = stock_value_date
        self.amount = amount
        self.number_of_stocks = self.amount / self.stock.value_at(self.stock_value_date)
        print(f"Creating grant with stock amount: {self.amount} number of stock sis {self.number_of_stocks}")
        self.cliffs_sorted_by_date = [
            (e.date, e.value * self.number_of_stocks * self.stock.value_at(e.date))
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
