"""Rule for replacing subject codes with readable names."""


def apply(event_data: dict, subjects: dict) -> None:
    """Replace the subject code with its configured display name."""

    subject = event_data["subject"]

    if subject in subjects:
        event_data["subject"] = subjects[subject]