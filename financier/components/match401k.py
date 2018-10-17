from .daily_reward import DailyReward


class Match401k(DailyReward):
    def __init__(
            self,
            yearly_income,
            match_percentage,
            match_contribution_per_dollar
    ):
        self.yearly_amount = (
            yearly_income
            * match_percentage
            * match_contribution_per_dollar
        )
