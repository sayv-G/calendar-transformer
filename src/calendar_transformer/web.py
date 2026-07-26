from fastapi import FastAPI, Response
from icalendar import Calendar
from .service import transform

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/calendar")
def calendar():
    calendar = Calendar()

    calendar = transform(
        calendar,
        {},
        {},
    )

    return Response(
        calendar.to_ical(),
        media_type="text/calendar",
    )