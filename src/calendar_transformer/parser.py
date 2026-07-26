def parse_summary(summary: str) -> dict:
    parts = summary.split("-")

    if len(parts) < 3:
        return {
            "type": "EVENT",
            "subject": summary,
            "class": "",
            "teacher": "",
        }

    return {
        "type": "LESSON",
        "subject": parts[0],
        "class": parts[1],
        "teacher": parts[2],
    }