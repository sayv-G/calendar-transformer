from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}

from fastapi import Response

@app.get("/calendar")
def calendar():
    return Response(
        "Not implemented",
        media_type="text/calendar",
    )