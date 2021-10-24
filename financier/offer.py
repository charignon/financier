import collections
from dataclasses import dataclass
import datetime
from typing import List, Iterable

from .components.component import Component


@dataclass(frozen=True)
class Offer:
    name: str
    components: Iterable[Component]

    @property
    def series_name(self) -> str:
        return f"{self.name} Gross Income"

    def value(self, start: datetime.date, finish: datetime.date) -> float:
        """Value of the offer between start and finish"""
        return sum(c.value(start, finish) for c in self.components)

    @property
    def components_pretty_name(self) -> List[str]:
        res = []
        component_count: collections.Counter[str] = collections.Counter()
        for c in self.components:
            if hasattr(c, "name") and c.name is not None:
                n = self.name + " " + c.name
            else:
                n = self.name + " " + c.__class__.__name__
            if n in component_count:
                name = f"{n}_{component_count[n]}"
            else:
                name = n
            component_count[n] += 1
            res.append(name)
        return res
