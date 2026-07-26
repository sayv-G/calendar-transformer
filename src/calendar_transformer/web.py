from fastapi import FastAPI, Response
from icalendar import Calendar
from .service import transform
from .calendar_io import load_calendar

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/calendar")
def calendar(url: str | None = None):
    if url is not None:
        return Response(
            "URL support not implemented yet",
            status_code=400,
        )

    calendar = load_calendar("data/Seifermann_Sola.ics")

    calendar = transform(
        calendar,
        {},
        {},
    )

    return Response(
        calendar.to_ical(),
        media_type="text/calendar",
    )