from .parser import parse_summary
from .transformer import transform_event


def transform_calendar(calendar, subjects, teachers):
    count = 0

    for event in calendar.walk("VEVENT"):
        summary = str(event.get("SUMMARY"))

        parsed = parse_summary(summary)

        print(parsed)

        parsed["subject"] = subjects.get(
            parsed["subject"],
            parsed["subject"]
        )

        parsed["teachers"] = [
            teachers.get(code, code)
            for code in parsed["teachers"]
        ]

        transform_event(event, parsed)

        count += 1

    return count