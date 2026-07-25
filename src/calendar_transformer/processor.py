from parser import parse_summary
from transformer import transform_event


def transform_calendar(calendar, subjects, teachers):
    count = 0

    for event in calendar.walk("VEVENT"):
        summary = str(event.get("SUMMARY"))

        parsed = parse_summary(summary)

        subject = subjects.get(
            parsed["subject"],
            parsed["subject"],
        )

        transform_event(
            event,
            parsed,
            subject,
            teachers,
        )

        count += 1

    return count