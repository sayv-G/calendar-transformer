from fastapi.testclient import TestClient

from calendar_transformer.web import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }

def test_calendar():
    response = client.get("/calendar")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/calendar")
    assert "BEGIN:VCALENDAR" in response.text