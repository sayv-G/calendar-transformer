def transform_event(event, parsed):
    original = str(event.get("SUMMARY"))

    if parsed["type"] != "LESSON":
        event["SUMMARY"] = parsed["subject"]
        return

    event["SUMMARY"] = parsed["subject"]

    description = f"""👩‍🏫 Lehrperson

{parsed["teacher"]}

🏫 Klasse

{parsed["class"]}

📝 Original

{original}
"""

    if "DESCRIPTION" in event:
        del event["DESCRIPTION"]

    event.add("DESCRIPTION", description)