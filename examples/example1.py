"""Example of how to use financier"""
import datetime

from financier import (
    Offer,
    plot_income,
    two_years_by_month,
)
from financier.components import (
    Match401k,
    FourYearsScheduleOneYearCliff,
    OneTimeBonus,
    Salary,
    StockGrant,
)


RAVIGA = Offer(
    'Raviga',
    Salary(yearly_amount=5000),
    StockGrant(
        amount=40000,
        schedule=FourYearsScheduleOneYearCliff(
            grant_date=datetime.date(2017, 2, 25)
        )
    ),
).detailed_income(
    date_range=two_years_by_month()
)

HOOLI = Offer(
    'Hooli',
    Salary(yearly_amount=15000),
    StockGrant(
        amount=10000,
        schedule=FourYearsScheduleOneYearCliff(
            grant_date=datetime.date(2017, 2, 25)
        )
    ),
    OneTimeBonus(amount=10000,
                 payoff_date=datetime.date(2019, 3, 5)),
    Match401k(yearly_income=150000,
              match_percentage=0.03,
              match_contribution_per_dollar=0.5),
).detailed_income(
    date_range=two_years_by_month()
)


def main():
    """Plot RAVIGA_VS_HOOLY to a file"""
    plot_filename = "raviga_vs_hooly.png"
    HOOLY.index = HOOLY.index.to_series().apply(lambda x:x.strftime("%b %y"))
    RAVIGA.index = RAVIGA.index.to_series().apply(lambda x:x.strftime("%b %y"))
    print(HOOLY)
    plot_income(HOOLY["Hooly Gross Income"].to_frame("Hooly Gross Income").join(
        RAVIGA["Raviga Gross Income"].to_frame("Raviga Gross Income")
    ), plot_filename)
    print(f"Check out {plot_filename}")

if __name__ == '__main__':
    main()
