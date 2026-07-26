from icalendar import Calendar

from .processor import transform_calendar


def transform(calendar: Calendar, subjects: dict, teachers: dict) -> Calendar:
    transform_calendar(
        calendar,
        subjects,
        teachers,
    )

    return calendar