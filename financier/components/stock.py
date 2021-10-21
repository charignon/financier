#!/usr/bin/env python3

import datetime

class Stock:
    def __init__(self, initial_value, initial_value_date = None, yearly_multiplier=1):
        self.initial_value = initial_value
        self.yearly_multiplier = yearly_multiplier
        self.daily_multiplier = self.yearly_multiplier ** (1/365)
        self.initial_value_date = initial_value_date or datetime.date.today()


    def value_at(self, date):
        day_since_start = (date - self.initial_value_date).days
        return self.initial_value * (self.daily_multiplier)**day_since_start
