from .daily_reward import DailyReward


class Salary(DailyReward):
    def __init__(self, yearly_amount, **kwargs):
        DailyReward.__init__(self, **kwargs)
        self.yearly_amount = yearly_amount
