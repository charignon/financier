import datetime
from typing import Dict, Any

from .component import Component


class DailyReward(Component):
    """A component that represents a daily reward, like a Salary"""

    yearly_amount: float

    def __init__(self, *args: Any, **kwargs: Dict[str, Any]):
        Component.__init__(self, *args, **kwargs)

    def pay_per_day(self) -> float:
        return float(self.yearly_amount) / 365

    def value(self, start: datetime.date, end: datetime.date) -> float:
        days = (end - start).days + 1
        return days * self.pay_per_day()
