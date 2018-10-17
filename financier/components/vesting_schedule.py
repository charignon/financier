"""Vesting schedules"""
import datetime


class VestingEvent:
    def __init__(self, date, value):
        self.date = date
        self.value = value


class BaseSchedule:
    """Abstract a vesting schedule
    You need to provide the following property when extending this class:
    - first_event_date
    - first_event_value
    - subsequent_events_spacing_weeks
    - subsequent_events_value
    - num_events
    """
    def __init__(self, grant_date):
        self.grant_date = grant_date
        self.first_event_value = None
        self.first_event_date = None
        self.subsequent_events_value = None
        self.subsequent_events_spacing_weeks = None
        self.num_events = None

    def nth_event(self, event_index):
        """Return the nth event"""
        if event_index == 0:
            return VestingEvent(
                date=self.first_event_date,
                value=self.first_event_value
            )

        delta = datetime.timedelta(
            weeks=self.subsequent_events_spacing_weeks * event_index
        )
        event_date = self.first_event_date + delta
        return VestingEvent(
            date=event_date,
            value=self.subsequent_events_value
        )

    @property
    def vesting_events(self):
        """Return the vesting events
        Returns:
          an iterable of events, that contain a date and value"""
        return [self.nth_event(n) for n in range(self.num_events)]


class FourYearsScheduleOneYearCliff(BaseSchedule):
    """A 4-year stock grant with one year vesting event"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_event_date = (
            self.grant_date + datetime.timedelta(weeks=52)
        )
        self.first_event_value = 1/4
        self.subsequent_events_value = 1/16
        self.subsequent_events_spacing_weeks = 13
        self.num_events = 13


class FourYearsScheduleNoCliff(BaseSchedule):
    """A 4-year stock grant with no vesting event"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_event_date = (
            self.grant_date + datetime.timedelta(weeks=13)
        )
        self.first_event_value = 1/16
        self.subsequent_events_value = 1/16
        self.subsequent_events_spacing_weeks = 13
        self.num_events = 16
