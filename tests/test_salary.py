"""Tests for the Salary component"""
import datetime
from financier.components import Salary


def test_salary_pay_per_day():
    """Check that the pay per day is computed properly"""
    assert Salary(yearly_amount=365000).pay_per_day() == 1000


def test_salary_value():
    """Check that the value over date ranges is correct"""
    value = Salary(yearly_amount=100000).value(
        start=datetime.date(2018, 6, 6), end=datetime.date(2018, 6, 10)
    )
    value = round(value, 0)
    assert value == 1370

    # Worked 1 day, start and end are inclusive!
    value = Salary(yearly_amount=365000).value(
        start=datetime.date(2018, 6, 6), end=datetime.date(2018, 6, 6)
    )
    value = round(value, 0)
    assert value == 1000
