#!/usr/bin/env python3

# A calculator projects the income over a period of time
from datetime import timedelta, date
import pandas as pd


def first_day_of_the_month(date):
    return date - timedelta(days=(date.day - 1))


def two_years_by_month():
    """Return a daterange of the 1st day of each month in the next two years"""
    start = first_day_of_the_month(date.today())
    return pd.date_range(start=start, periods=25, freq="MS").date


def four_years_by_month():
    """Return a daterange of the 1st day of each month in the next four years"""
    start = first_day_of_the_month(date.today())
    return pd.date_range(start=start, periods=49, freq="MS").date


def gen_intervals(start_dates):
    """Generate non-overlapping intervals covering `date_range`"""
    end_dates = [d - timedelta(days=1) for d in start_dates]
    return list(zip(start_dates[:-1], end_dates[1:]))


def identity(x):
    return x

class Calculator:
    @staticmethod
    def detailed_income(offer, date_range, agg_fn=identity):
        """Return income aggregated over date_range w/ agg_fn as a dataframe"""
        income_by_period = []
        for i in gen_intervals(date_range):
            total = round(offer.value(*i))
            by_component = [round(c.value(*i)) for c in offer.components]
            income_by_period.append(by_component + [total])

        aggregate_income = agg_fn(income_by_period)

        # Drop the last entry as we have one fewer interval than start dates
        index = pd.Series(date_range[:-1], name="Date")
        return pd.DataFrame(
            aggregate_income,
            index,
            columns=offer.components_pretty_name + [offer.series_name]
        )

    @staticmethod
    def income(offer, date_range, agg_fn=identity):
        """Return income aggregated over date_range w/ agg_fn as a dataframe"""
        income_by_period = [offer.value(*i) for i in gen_intervals(date_range)]
        aggregate_income = agg_fn(income_by_period)

        # Drop the last entry as we have one fewer interval than start dates
        index = pd.Series(date_range[:-1], name="Date")
        return pd.Series(aggregate_income, index).to_frame(offer.series_name)

    @staticmethod
    def cumulative_income(offer, date_range):
        """Return income dataframe cumulative by period over date_range"""
        return Calculator.income(agg_fn=np.cumsum, date_range=date_range)
