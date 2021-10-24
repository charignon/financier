"""Vesting schedules"""
import datetime
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class VestingEvent:
    date: datetime.date
    value: float


@dataclass(frozen=True)
class Schedule:
    grant_date: datetime.date
    first_event_value: float
    first_event_date: datetime.date
    subsequent_events_value: float
    subsequent_events_spacing_weeks: int
    num_events: int

    def nth_event(self, n: int) -> VestingEvent:
        if n == 0:
            return VestingEvent(
                date=self.first_event_date, value=self.first_event_value
            )

        delta = datetime.timedelta(weeks=self.subsequent_events_spacing_weeks * n)
        event_date = self.first_event_date + delta
        return VestingEvent(date=event_date, value=self.subsequent_events_value)

    @property
    def vesting_events(self) -> List[VestingEvent]:
        return [self.nth_event(n) for n in range(self.num_events)]


def four_year_schedule_one_year_cliff(grant_date: datetime.date) -> Schedule:
    return Schedule(
        grant_date=grant_date,
        first_event_date=grant_date + datetime.timedelta(weeks=52),
        first_event_value=1 / 4,
        subsequent_events_value=1 / 16,
        subsequent_events_spacing_weeks=13,
        num_events=13,
    )


def one_year_schedule_no_cliff(grant_date: datetime.date) -> Schedule:
    return Schedule(
        grant_date=grant_date,
        first_event_date=grant_date + datetime.timedelta(weeks=13),
        first_event_value=1 / 4,
        subsequent_events_value=1 / 4,
        subsequent_events_spacing_weeks=13,
        num_events=4,
    )


def one_year_schedule_one_year_cliff(grant_date: datetime.date) -> Schedule:
    return Schedule(
        grant_date=grant_date,
        first_event_date=grant_date + datetime.timedelta(weeks=52),
        first_event_value=1,
        subsequent_events_value=0,
        subsequent_events_spacing_weeks=0,
        num_events=1,
    )


def four_year_schedule_no_cliff(grant_date: datetime.date) -> Schedule:
    return Schedule(
        grant_date=grant_date,
        first_event_date=grant_date + datetime.timedelta(weeks=13),
        first_event_value=1 / 16,
        subsequent_events_value=1 / 16,
        subsequent_events_spacing_weeks=13,
        num_events=16,
    )
