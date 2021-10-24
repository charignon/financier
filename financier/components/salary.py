from .daily_reward import DailyReward
from typing import Any


class Salary(DailyReward):
    def __init__(self, yearly_amount: int, **kwargs: Any):
        DailyReward.__init__(self, **kwargs)
        self.yearly_amount = yearly_amount
