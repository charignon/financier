#!/usr/bin/env python

from financier.components import StockGrant
from financier.components import FourYearsScheduleOneYearCliff
from financier.components import FourYearsScheduleNoCliff
import datetime


def test_is_whole_grant_distributed_with_cliff():
    """Check that exactly the whole grant is distributed."""
    grant_date = datetime.date(2017, 2, 25)
    for sched in [
            FourYearsScheduleOneYearCliff(grant_date=grant_date),
            FourYearsScheduleNoCliff(grant_date=grant_date)
    ]:
        s = StockGrant(amount=800000, schedule=sched)
        acc = 0
        for u in range(5000):
            start = grant_date + datetime.timedelta(weeks=u)
            end = start + datetime.timedelta(days=6)
            acc += s.value(start, end)
        assert acc == 800000, "Error with %s %s" % (sched,
                                                    sched.iterator())


# Check that the NoCliff grant after 6 months grants 1/8th of the total
# and that the cliff grant grants 0 after 6 month
def test_after_six_month_no_cliff():
    """Check that exactly the whole grant is distributed."""
    grant_date = datetime.date(2017, 2, 25)
    sched = FourYearsScheduleNoCliff(grant_date=grant_date)
    s = StockGrant(amount=800000, schedule=sched)
    e = grant_date + datetime.timedelta(weeks=26, days=1)
    assert s.value(grant_date, e) == 100_000


def test_after_six_month_cliff():
    """Check that exactly the whole grant is distributed."""
    grant_date = datetime.date(2017, 2, 25)
    sched = FourYearsScheduleOneYearCliff(grant_date=grant_date)
    s = StockGrant(amount=800000, schedule=sched)
    e = grant_date + datetime.timedelta(weeks=26, days=1)
    assert s.value(grant_date, e) == 0
