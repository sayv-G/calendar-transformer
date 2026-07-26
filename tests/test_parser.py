from calendar_transformer.parser import parse_summary


def test_single_lesson():
    parsed = parse_summary("AA-1UGc-MarDan")

    assert parsed["type"] == "LESSON"
    assert parsed["subject"] == "AA"
    assert parsed["classes"] == ["1UGc"]
    assert parsed["teachers"] == ["MarDan"]


def test_multiple_teachers():
    parsed = parse_summary("TGWE-1UGc-BluPat,JooGra")

    assert parsed["teachers"] == [
        "BluPat",
        "JooGra",
    ]


def test_multiple_classes():
    parsed = parse_summary("SMD-1UGa,1UGc-GreCla")

    assert parsed["classes"] == [
        "1UGa",
        "1UGc",
    ]


def test_event():
    parsed = parse_summary("Einführung")

    assert parsed["type"] == "EVENT"
    assert parsed["subject"] == "Einführung"
    assert parsed["classes"] == []
    assert parsed["teachers"] == []