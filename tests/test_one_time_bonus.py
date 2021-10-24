"""Tests for the OneTimeBonus component"""
import datetime
from financier.components import OneTimeBonus


def test_one_time_bonus_value():
    """Check that the value over date ranges is correct
    Over 5 years, get the bonus, not more, only one week has the bonus"""
    base_date = datetime.date(2018, 1, 1)
    payoff_date = datetime.date(2018, 6, 6)
    bonus_amount = 100000
    bonus = OneTimeBonus(amount=bonus_amount, payoff_date=payoff_date)

    num_diff_zero = 0
    acc = 0
    for d in range(52 * 5):
        start = base_date + datetime.timedelta(weeks=d)
        end = start + datetime.timedelta(days=6)
        v = bonus.value(start, end)
        if v != 0:
            num_diff_zero += 1
        acc += v

    assert acc == bonus_amount
    assert num_diff_zero == 1
