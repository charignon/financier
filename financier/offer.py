import pandas as pd
import numpy as np
import collections
from .calculator import Calculator


class Offer:
    def __init__(self, name, *components):
        self.name = name
        self.series_name = f"{self.name} Gross Income"
        self.components = components
        for c in components:
            assert hasattr(c, "value"), f"{c} is not a component!"

    def value(self, start, finish):
        """Value of the offer between start and finish"""
        return sum(c.value(start, finish) for c in self.components)

    @property
    def components_pretty_name(self):
        res = []
        component_count = collections.Counter()
        for c in self.components:
            if hasattr(c, "name") and c.name is not None:
                n = self.name + " " + c.name
            else:
                n = self.name + " " +c.__class__.__name__
            if n in component_count:
                name = f"{n}_{component_count[n]}"
            else:
                name = n
            component_count[n] += 1
            res.append(name)
        return res
