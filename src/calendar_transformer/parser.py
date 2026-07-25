def parse_summary(summary: str) -> dict:
    parts = summary.split("-")

    if len(parts) < 3:
        return {
            "subject": summary,
            "class": "",
            "teacher": "",
        }

    return {
        "subject": parts[0],
        "class": parts[1],
        "teacher": parts[2],
    }