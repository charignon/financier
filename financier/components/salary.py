from .daily_reward import DailyReward


class Salary(DailyReward):
    def __init__(self, yearly_amount):
        self.yearly_amount = yearly_amount
