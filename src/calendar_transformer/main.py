from pathlib import Path

from icalendar import Calendar

from config import load_yaml
from parser import parse_summary
from transformer import transform_event

subjects = load_yaml("subjects.yaml")
teachers = load_yaml("teachers.yaml")

ics_file = Path("data/Seifermann_Sola.ics")

with open(ics_file, "rb") as f:
    cal = Calendar.from_ical(f.read())

count = 0

for event in cal.walk("VEVENT"):
    summary = str(event.get("SUMMARY"))

    parsed = parse_summary(summary)

    subject = subjects.get(parsed["subject"], parsed["subject"])

    transform_event(event, parsed, subject, teachers)

    count += 1

with open("data/output.ics", "wb") as f:
    f.write(cal.to_ical())

print(f"✅ {count} Termine verarbeitet.")
print("💾 Neue Datei gespeichert: data/output.ics")