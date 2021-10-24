import datetime
from typing import Dict, Any

from .component import Component


class OneTimeBonus(Component):
    def __init__(
        self, amount: int, payoff_date: datetime.date, **kwargs: Dict[str, Any]
    ):
        Component.__init__(self, **kwargs)
        self.amount = amount
        self.payoff_date = payoff_date

    def value(self, start: datetime.date, end: datetime.date) -> int:
        if self.payoff_date >= start and self.payoff_date <= end:
            return self.amount
        return 0
