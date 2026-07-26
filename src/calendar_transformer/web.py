from fastapi import FastAPI, Response
from icalendar import Calendar

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/calendar")
def calendar():
    calendar = Calendar()

    return Response(
        calendar.to_ical(),
        media_type="text/calendar",
    )