from typing import Any

from .daily_reward import DailyReward


class Match401k(DailyReward):
    def __init__(
        self,
        yearly_income: float,
        match_percentage: float,
        match_contribution_per_dollar: float,
        **kwargs: Any
    ):
        DailyReward.__init__(self, **kwargs)
        self.yearly_amount = (
            yearly_income * match_percentage * match_contribution_per_dollar
        )
