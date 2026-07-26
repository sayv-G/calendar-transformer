from icalendar import Event

from calendar_transformer.transformer import transform_event


def test_lesson_summary():
    event = Event()
    event.add("SUMMARY", "AA MarDan 1UGc")

    parsed = {
        "type": "LESSON",
        "subject": "Mathematik",
        "teachers": ["Daniel Martin"],
        "classes": ["1UGc"],
    }

    transform_event(event, parsed)

    assert event["SUMMARY"] == "Mathematik"

def test_lesson_description():
    event = Event()
    event.add("SUMMARY", "AA MarDan 1UGc")

    parsed = {
        "type": "LESSON",
        "subject": "Mathematik",
        "teachers": ["Daniel Martin"],
        "classes": ["1UGc"],
    }

    transform_event(event, parsed)

    description = str(event["DESCRIPTION"])

    assert "Daniel Martin" in description
    assert "1UGc" in description
    assert "AA MarDan 1UGc" in description

def test_event_summary():
    event = Event()
    event.add("SUMMARY", "Einführung")

    parsed = {
        "type": "EVENT",
        "subject": "Einführung",
        "teachers": [],
        "classes": [],
    }

    transform_event(event, parsed)

    assert event["SUMMARY"] == "Einführung"
    assert "DESCRIPTION" not in event