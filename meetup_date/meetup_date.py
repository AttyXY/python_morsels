from datetime import date
from calendar import monthcalendar, monthrange
from pandas.tseries.holiday import USFederalHolidayCalendar


def get_day(year: int, month: int, nth: int, weekday: int) -> date:
    """Returns the numeric day of the given weekday of the nth nth of the
    given year and month.

    assumptions
    ---
    1 <= nth <= 5 or - 5 <= nth <= -1
    1 <= weekday <= 7
    1 <= day <= 31

    tests
    ---
    >>> get_day(2012, 3, 4, 4)
    datetime.date(2012, 3, 22)
    >>> get_day(2017, 7, 1, 2)  # first Tues on 2nd week
    datetime.date(2017, 7, 4)
    >>> get_day(2017, 7, 5, 1)  # fifth Mon on 6th week
    datetime.date(2017, 7, 31)
    >>> get_day(2017, 7, 4, 1)  # fourth Mon on 5th week
    datetime.date(2017, 7, 24)
    >>> get_day(2017, 7, 1, 6)  # first Sat on 1st week
    datetime.date(2017, 7, 1)
    """
    weeks = monthcalendar(year, month)

    counter = 0
    while nth:
        counter += 1
        nth_week = weeks[counter - 1]
        day = nth_week[weekday - 1]
        if day == 0:
            continue
        else:
            nth -= 1

    return date(year=year, month=month, day=day)


def meetup_date(year: int, month: int, nth: int = 4, weekday: int = 4) -> date:
    """Returns fourth Thursday of the month (excluding US holidays).

    assumptions
    ---
    1 <= year < 9999    # based on datetime.MINYEAR/MAXYEAR
    1 <= month <= 12
    1 <= nth <= 5 or - 5 <= nth <= -1
    1 <= weekday <= 7   # based on date.isoweekday

    tests
    ---
    base
    >>> print(meetup_date(2012, 3))
    2012-03-22
    >>> print(meetup_date(2015, 2))
    2015-02-26
    >>> print(meetup_date(2018, 6))
    2018-06-28
    >>> print(meetup_date(2020, 1))
    2020-01-23

    bonus 1
    >>> print("SD Python:", meetup_date(2015, 8, nth=4, weekday=4))
    SD Python: 2015-08-27
    >>> print("PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=3))
    PyLadies on 4th Wed: 2018-07-25
    >>> print("SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=2))
    SDJS on 1st Tues: 2012-02-07
    """

    last_day_of_month = monthrange(year, month)[1]
    holidays = USFederalHolidayCalendar().holidays(
                    start=f"{year}-{month}-01",
                    end=f"{year}-{month}-{last_day_of_month}"
               ).to_pydatetime()

    day = get_day(year, month, nth, weekday)
    while day in holidays:
        if day + 7 <= last_day_of_month:
            # reschedule to next week
            day = get_day(year, month, nth + 1, weekday)
        else:
            # reschedule to first week of next month
            day = get_day(year, month + 1, 1, weekday)

    return day
