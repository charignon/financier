"""Tests for the Offer modules"""
from datetime import date
import hashlib
import os
import tempfile

from financier.offer import (
    Offer,
    first_day_of_the_month,
    two_years_by_month,
    gen_intervals,
    plot_income,
)
from financier.components import (
    Match401k,
    FourYearsScheduleOneYearCliff,
    OneTimeBonus,
    Salary,
    StockGrant,
)


def test_first_day_of_the_month():
    assert (date(2019, 2, 1) == first_day_of_the_month(date(2019, 2, 10)))
    assert (date(2019, 2, 1) == first_day_of_the_month(date(2019, 2, 1)))
    assert (date(2019, 1, 1) == first_day_of_the_month(date(2019, 1, 31)))


def test_two_years_by_month():
    # 25 start dates, hence 24 monthly intervals
    assert 25 == len(two_years_by_month())


def test_gen_interval():
    # 25 start dates, hence 24 monthly intervals
    intervals = gen_intervals(two_years_by_month())
    assert 24 == len(intervals)


def md5_file(fname):
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def test_value():
    offer = Offer(
        'Raviga',
        Salary(yearly_amount=36500),
        Match401k(36500, 0.10, 1)
    )

    # (100 per day + 10 per day) x 10 == 1100
    # 10 dollar because 100 per day * 10% match
    assert offer.value(date(2019, 1, 1), date(2019, 1, 10)) == 1100


def test_plot_income():
    RAVIGA = Offer(
        'Raviga',
        Salary(yearly_amount=124000),
        StockGrant(
            amount=800000,
            schedule=FourYearsScheduleOneYearCliff(
                grant_date=date(2017, 2, 25)
            )
        ),
    ).income(
        date_range=two_years_by_month()
    )

    HOOLY = Offer(
        'Hooly',
        Salary(yearly_amount=150000),
        StockGrant(
            amount=83322,
            schedule=FourYearsScheduleOneYearCliff(
                grant_date=date(2017, 2, 25)
            )
        ),
        OneTimeBonus(amount=10000,
                     payoff_date=date(2019, 3, 15)),
        Match401k(yearly_income=150000,
                  match_percentage=0.03,
                  match_contribution_per_dollar=0.5),
    ).income(
        date_range=two_years_by_month()
    )
    with tempfile.TemporaryDirectory() as tmpdirname:
        plot_filename = os.path.join(tmpdirname, "raviga_vs_hooly.png")
        plot_income(HOOLY.join(RAVIGA), plot_filename)
        expected_md5 = "851b52467af0ac1a52a6073e6b84a1c1"
        assert md5_file(plot_filename) == expected_md5
