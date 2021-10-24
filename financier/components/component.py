#!/usr/bin/env python3
import datetime
from typing import Any


class Component:
    def __init__(self, *args: Any, **kwargs: Any):
        if "name" in kwargs:
            self.name: str = kwargs["name"]

    def value(self, start: datetime.date, finish: datetime.date) -> float:
        ...
