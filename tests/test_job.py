import pytest

from app.domain import Job


def test_should_create_a_job():
    # When
    job = Job(1, "Dev")

    # Then
    assert job.id == 1
    assert job.name == "Dev"


def test_should_fail_if_id_negative():
    # When negative, then raise ValueError
    with pytest.raises(ValueError):
        Job(-1, "Dev")


def test_should_fail_if_name_is_empty():
    # When empty, then raise ValueError
    with pytest.raises(ValueError):
        Job(1, "   ")