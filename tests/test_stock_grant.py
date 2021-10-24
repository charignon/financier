#!/usr/bin/env python

from financier.components import (
    StockGrant,
    Stock,
    four_year_schedule_one_year_cliff,
    four_year_schedule_no_cliff,
)
import datetime


def test_is_whole_grant_distributed_with_cliff():
    """Check that exactly the whole grant is distributed."""
    grant_date = datetime.date(2017, 2, 25)
    for sched in [
        four_year_schedule_one_year_cliff(grant_date=grant_date),
        four_year_schedule_no_cliff(grant_date=grant_date),
    ]:
        s = StockGrant(amount=800000, schedule=sched)
        acc = 0
        for u in range(5000):
            start = grant_date + datetime.timedelta(weeks=u)
            end = start + datetime.timedelta(days=6)
            acc += s.value(start, end)
        assert acc == 800000, "Error with %s %s" % (sched, sched.iterator())


# Check that the NoCliff grant after 6 months grants 1/8th of the total
# and that the cliff grant grants 0 after 6 month
def test_after_six_month_no_cliff():
    """Check that exactly the whole grant is distributed."""
    grant_date = datetime.date(2017, 2, 25)
    sched = four_year_schedule_no_cliff(grant_date=grant_date)
    s = StockGrant(amount=800000, schedule=sched)
    e = grant_date + datetime.timedelta(weeks=26, days=1)
    assert s.value(grant_date, e) == 100_000


def test_after_six_month_cliff():
    """Check that exactly the whole grant is distributed."""
    grant_date = datetime.date(2017, 2, 25)
    sched = four_year_schedule_one_year_cliff(grant_date=grant_date)
    s = StockGrant(amount=800000, schedule=sched)
    e = grant_date + datetime.timedelta(weeks=26, days=1)
    assert s.value(grant_date, e) == 0


def test_stock_value_no_growth():
    s = Stock(
        initial_value=100,
        initial_value_date=datetime.date(2017, 2, 25),
    )
    assert s.value_at(datetime.date(2020, 1, 1)) == 100


def test_stock_value_two_year_growth():
    s = Stock(
        initial_value=100,
        yearly_multiplier=1.68,
        initial_value_date=datetime.date(2017, 2, 25),
    )
    assert abs(s.value_at(datetime.date(2019, 2, 25)) - 100 * 1.68 * 1.68) < 1


def test_stock_value_six_month_growth():
    s = Stock(
        initial_value=100,
        yearly_multiplier=1.68,
        initial_value_date=datetime.date(2017, 2, 25),
    )
    assert abs(s.value_at(datetime.date(2017, 8, 25)) - 129.3) < 1
