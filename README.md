# Financier

Model compensation packages with python. Can be useful to compare job offers.

```python
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
    Match401k(yearly_income=15_0000,
              match_percentage=0.03,
              match_contribution_per_dollar=0.5),
)

plot_income(
    Calculator.cummulative_income(
        offer = HOOLI,
        date_range=four_years_by_month()
    ), "/tmp/hooli.png"
)
```
![Hooli offer cumulative income](/assets/hoolicum.png)

## Installation

### Installing with pip

This package is not yet published via pypi.

### Manual installation from git

Clone the repo and set up a virtualenv:
```shell
git clone git@github.com:charignon/financier
cd financier
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```

### Run the example:

```shell
PYTHONPATH=.:$PYTHONPATH python examples/example1.py
```
## Usage

See my [blog post](https://blog.laurentcharignon.com/post/financier-modeling-compensation-python/) for more information.

## Contributing
### Running the tests

```shell
py.test
```
## Origin of the name financier

It is a french adjective that means "related to finance".
