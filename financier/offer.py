import pandas as pd
import numpy as np
from datetime import timedelta, date
import collections


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

    def detailed_income(self, date_range, agg_fn=identity):
        """Return income aggregated over date_range w/ agg_fn as a dataframe"""
        income_by_period = []
        for i in gen_intervals(date_range):
            total = round(self.value(*i))
            by_component = [round(c.value(*i)) for c in self.components]
            income_by_period.append(by_component + [total])

        aggregate_income = agg_fn(income_by_period)

        # Drop the last entry as we have one fewer interval than start dates
        index = pd.Series(date_range[:-1], name="Date")
        return pd.DataFrame(
            aggregate_income,
            index,
            columns=self.components_pretty_name + [self.series_name]
        )

    def income(self, date_range, agg_fn=identity):
        """Return income aggregated over date_range w/ agg_fn as a dataframe"""
        income_by_period = [self.value(*i) for i in gen_intervals(date_range)]
        aggregate_income = agg_fn(income_by_period)

        # Drop the last entry as we have one fewer interval than start dates
        index = pd.Series(date_range[:-1], name="Date")
        return pd.Series(aggregate_income, index).to_frame(self.series_name)

    def cumulative_income(self, date_range):
        """Return income dataframe cumulative by period over date_range"""
        return self.income(agg_fn=np.cumsum, date_range=date_range)


def plot_income(df, fname=None):
    """Plot an offer df, if fname is None save to a file named fname"""
    import matplotlib
    from matplotlib import pyplot as plt
    ax = df.plot(kind="bar", figsize=(20, 6), fontsize=15)
    ax.set_yticks((range(0, int(df.max()[0]), 50000)), minor=True)
    ax.grid(True, which='minor', axis='y')
    ax.set_ylabel("$ Amount")
    plt.tight_layout()
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    if fname is None:
        plt.show()
    else:
        plt.savefig(fname)
