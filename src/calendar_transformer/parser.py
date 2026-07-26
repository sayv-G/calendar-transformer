def parse_summary(summary: str) -> dict:
    parts = summary.split("-")

    if len(parts) < 3:
        return {
            "type": "EVENT",
            "subject": summary,
            "classes": [],
            "teachers": [],
        }

    return {
        "type": "LESSON",
        "subject": parts[0],
        "classes": parts[1].split(","),
        "teachers": parts[2].split(","),
    }