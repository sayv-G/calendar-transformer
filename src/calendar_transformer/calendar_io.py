from pathlib import Path

import requests
from icalendar import Calendar


def load_calendar(source):
    """
    Lädt einen Kalender aus einer lokalen Datei oder einer URL.
    """

    if source.startswith(("http://", "https://")):
        print("🌐 Lade Kalender von URL...")

        response = requests.get(source, timeout=30)
        response.raise_for_status()

        return Calendar.from_ical(response.content)

    print("📂 Lade lokale Datei...")

    with open(Path(source), "rb") as f:
        return Calendar.from_ical(f.read())


def save_calendar(calendar, filename):
    """
    Speichert einen Kalender als ICS-Datei.
    """

    with open(Path(filename), "wb") as f:
        f.write(calendar.to_ical())