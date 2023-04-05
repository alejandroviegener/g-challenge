import pytest 

from app.domain import Department

def test_should_create_a_department():
    # When
    department = Department(1, "Dev")

    # Then
    assert department.id == 1
    assert department.name == "Dev"


def test_should_fail_if_id_negative():
    # When negative, then raise ValueError
    with pytest.raises(ValueError):
        Department(-1, "Dev")


def test_should_fail_if_name_is_empty():
    # When empty, then raise ValueError
    with pytest.raises(ValueError):
        Department(1, "   ")