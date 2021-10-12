"""Example of how to use financier"""
import datetime

from financier import (
    Offer,
    two_years_by_month,
)
from financier.components import (
    FourYearsScheduleOneYearCliff,
    PeriodicBonus,
    Salary,
    StockGrant,
)


RAVIGA = Offer(
    'Raviga',
    Salary(yearly_amount=5000),
    PeriodicBonus(amount=10000,
                  name="Wellness budget",
                  date_seq=[datetime.date(2017,8,8)]),
    StockGrant(
        amount=40000,
        schedule=FourYearsScheduleOneYearCliff(
            grant_date=datetime.date(2017, 2, 25)
        )
    ),
).detailed_income(
    date_range=two_years_by_month()
)

def main():
    """Export RAVIGA as CSV"""
    plot_filename = "raviga.csv"
    RAVIGA.index = RAVIGA.index.to_series().apply(lambda x:x.strftime("%b %y"))
    RAVIGA.to_csv(plot_filename)
    print(f"Check out {plot_filename}")

if __name__ == '__main__':
    main()
