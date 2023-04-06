
import pytest

from app.domain import Employee


def test_should_create_new_employee():
    
    # When 
    employee = Employee(1, "John", "Doe", "2022-12-31", 2, 3)

    # Then
    assert employee.id == 1
    assert employee.first_name == "John"
    assert employee.last_name == "Doe"
    assert employee.hiring_date == "2022-12-31"
    assert employee.job_id == 2
    assert employee.department_id == 3



@pytest.mark.parametrize("hiring_date", ["2022-12", "2022-12-31 12:00:00", "2022-12-31T12:00:00", " "])
def test_should_fail_if_hiring_date_not_iso_format(hiring_date):
    # When not iso, then raise ValueError
    with pytest.raises(ValueError):
        Employee(1, "John", "Doe", hiring_date, 2, 3)


def test_should_fail_if_id_negative():
    # When negative, then raise ValueError
    with pytest.raises(ValueError):
        Employee(-1, "John", "Doe", "2022-12-31", 2, 3)


def test_should_not_fail_if_id_is_zero():
    # When zero, then no raise
    e = Employee(0, "John", "Doe", "2022-12-31", 2, 3)
    assert e.id == 0


def test_should_fail_if_first_name_empty():
    # When empty, then raise ValueError
    with pytest.raises(ValueError):
        Employee(1, "   ", "Doe", "2022-12-31", 2, 3)

def test_should_fail_if_last_name_empty():
    # When empty, then raise ValueError
    with pytest.raises(ValueError):
        Employee(1, "John", "   ", "2022-12-31", 2, 3)

def test_should_fail_if_employee_job_id_is_negative():
    # When negative, then raise ValueError
    with pytest.raises(ValueError):
        Employee(1, "John", "Doe", "2022-12-31", -1, 3)


def test_should_fail_if_deparment_id_is_negative():
    # When negative, then raise ValueError
    with pytest.raises(ValueError):
        Employee(1, "John", "Doe", "2022-12-31", 2, -1)