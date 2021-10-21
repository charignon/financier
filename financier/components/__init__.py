"""Components modules

Components represents the different part of an offer, for example a Salary, a Bonus or a StockGrant.
Components have to conform to the following specification:

class ComponentA:
    def value(self, start, end):
        return the_value_of_the_component_between_start_and_end_inclusive

Example:

class OneTimeBonus:
    def __init__(self, amount, payoff_date):
        self.amount = amount
        self.payoff_date = payoff_date

    def value(self, start, end):
        if self.payoff_date >= start and self.payoff_date <= end:
            return self.amount
        return 0

"""
from .salary import Salary
from .daily_reward import DailyReward
from .stock_grant import StockGrant
from .vesting_schedule import FourYearsScheduleOneYearCliff
from .vesting_schedule import FourYearsScheduleNoCliff
from .vesting_schedule import OneYearScheduleNoCliff
from .vesting_schedule import OneYearScheduleWithCliff
from .one_time_bonus import OneTimeBonus
from .periodic_bonus import PeriodicBonus
from .match401k import Match401k
from .stock import Stock
