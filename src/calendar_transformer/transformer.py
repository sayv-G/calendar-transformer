def transform_event(event, parsed):
    original = str(event.get("SUMMARY"))

    if parsed["type"] != "LESSON":
        event["SUMMARY"] = parsed["subject"]
        return

    event["SUMMARY"] = parsed["subject"]

    teacher_text = "\n".join(parsed["teachers"])
    class_text = "\n".join(parsed["classes"])

    description = f"""👩‍🏫 Lehrperson

{teacher_text}

🏫 Klasse

{class_text}

📝 Original

{original}
"""

    if "DESCRIPTION" in event:
        del event["DESCRIPTION"]

    event.add("DESCRIPTION", description)