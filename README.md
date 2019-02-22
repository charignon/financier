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

plot_income(HOOLI.cummulative_income(
    date_range=four_years_by_month()
), "/tmp/hooli.png")
```
![Hooli offer cummulative income](/assets/hoolicum.png)

## Installation

### Installing with pip
TODO

### Manual installation from git

Clone the repo and set up a virtualenv:
```shell
git clone git@github.com:charignon/financier
cd financier
python3 -m venv .
source bin/activate
source bin/activate
pip install -r requirements.txt
```

### Run the example:

```shell
python examples/example1.py
```
## Usage

See blog post: XXX

## Contributing
### Running the tests

```shell
py.test
```
## Origin of the name financier

It is a french adjective that means "related to finance".
