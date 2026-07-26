from icalendar import Calendar, Event

from calendar_transformer.processor import transform_calendar


def test_transform_calendar():
    calendar = Calendar()

    event = Event()
    event.add("SUMMARY", "AA-1UGc-MarDan")

    calendar.add_component(event)

    subjects = {
        "AA": "Mathematik",
    }

    teachers = {
        "MarDan": "Daniel Martin",
    }

    count = transform_calendar(
        calendar,
        subjects,
        teachers,
    )

    assert count == 1

    events = calendar.walk("VEVENT")
    assert len(events) == 1
    event = events[0]

    assert event["SUMMARY"] == "Mathematik"

    description = str(event["DESCRIPTION"])

    assert "Daniel Martin" in description
    assert "1UGc" in description
    assert "AA-1UGc-MarDan" in description