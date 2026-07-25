def transform_event(event, parsed, subject, teachers):
    original = str(event.get("SUMMARY"))

    teacher = teachers.get(parsed["teacher"], parsed["teacher"])

    event["SUMMARY"] = subject

    description = f"""👨‍🏫 Lehrperson
{teacher}

🏫 Klasse
{parsed['class']}

📝 Original
{original}
"""

    if "DESCRIPTION" in event:
        del event["DESCRIPTION"]

    event.add("DESCRIPTION", description)