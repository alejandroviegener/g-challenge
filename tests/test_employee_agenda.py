
from typing import List

import pytest

from app.domain import Employee, Job, Department
from app.agenda import EmployeeAgenda


def test_should_be_able_to_add_employees_in_empty_agenda():

    # Given
    employees = [
        Employee(1, "John", "Doe", "2022-12-31", Job(2, "Software Engineer"), Department(1, "IT")), 
        Employee(2, "Jane", "Doe", "2022-12-31", Job(2, "Software Engineer"), Department(1, "IT")),
        Employee(3, "John", "Doe", "2022-12-31", Job(3, "Data Scientist"), Department(1, "IT"))
    ]

    # When
    employee_agenda = EmployeeAgenda()
    employee_agenda.add_employees(employees)

    # Then
    assert employee_agenda.size() == (3, 2, 1)


def test_should_fail_if_adding_employee_with_existing_id():

    # Given
    employee_agenda = EmployeeAgenda()

    # When
    original_employee = Employee(1, "John", "Doe", "2022-12-31", Job(2, "Software Engineer"), Department(3, "IT"))
    employee_agenda.add_employees([original_employee])
    
    # Then
    with pytest.raises(ValueError):
        employee = Employee(1, "NoJohn", "NoDoe", "2022-12-31", Job(2, "Software Engineer"), Department(3, "IT"))
        employee_agenda.add_employees([employee])

    assert employee_agenda.get_employee(1) == original_employee


def test_should_fail_if_employee_job_inconsistent_with_agenda():
    """A job is incosistent if it is in the agenda asociated to another employee, it has the same id but different values"""

    ## Given
    employees = [
        Employee(1, "John", "Doe", "2022-11-30", Job(2, "Software Engineer"), Department(1, "IT")), 
        Employee(2, "Jane", "Doe", "2022-10-30", Job(2, "Software Engineer"), Department(1, "IT")),
        Employee(3, "John", "Doe", "2022-12-24", Job(3, "Data Scientist"), Department(1, "IT"))
    ]
    employee_agenda = EmployeeAgenda()
    employee_agenda.add_employees(employees)
    
    # When
    with pytest.raises(ValueError):
        employee = Employee(4, "Alex", "Doe", "2022-12-31", Job(2, "Software Developer (not Engineer)"), Department(1, "IT"))
        employee_agenda.add_employees([employee])

    # Then
    assert employee_agenda.size() == (3, 2, 1)


def test_should_fail_if_employee_department_inconsistent_with_agenda():
    """A department is incosistent if it is in the agenda asociated to another employee, it has the same id but different values"""

    ## Given
    employees = [
        Employee(1, "John", "Doe", "2022-11-30", Job(2, "Software Engineer"), Department(1, "IT")), 
        Employee(2, "Jane", "Doe", "2022-10-30", Job(2, "Software Engineer"), Department(1, "IT")),
        Employee(3, "John", "Doe", "2022-12-24", Job(3, "Data Scientist"), Department(1, "IT"))
    ]
    employee_agenda = EmployeeAgenda()
    employee_agenda.add_employees(employees)
    
    # When
    with pytest.raises(ValueError):
        employee = Employee(4, "Alex", "Doe", "2022-12-31", Job(2, "Software Engineer"), Department(1, "I.T."))
        employee_agenda.add_employees([employee])

    # Then
    assert employee_agenda.size() == (3, 2, 1)

    
def test_should_rollback_entire_transaction_if_add_fails_for_some_employees():
    ## Given
    employees = [
        Employee(1, "John", "Doe", "2022-11-30", Job(2, "Software Engineer"), Department(1, "IT")), 
        Employee(2, "Jane", "Doe", "2022-10-30", Job(2, "Software Engineer"), Department(1, "IT")),
        Employee(3, "John", "Doe", "2022-12-24", Job(3, "Data Scientist"), Department(1, "IT"))
    ]
    employee_agenda = EmployeeAgenda()
    employee_agenda.add_employees(employees)
    
    # When
    with pytest.raises(ValueError):
        new_employees = [
            Employee(4, "John", "Doe", "2022-11-30", Job(2, "Software Engineer"), Department(1, "IT")), 
            Employee(5, "Jane", "Doe", "2022-10-30", Job(2, "Software Engineer"), Department(1, "IT")),
            Employee(2, "John", "Doe", "2022-12-24", Job(3, "Data Scientist"), Department(1, "IT"))
        ]
        employee_agenda.add_employees(new_employees)

    # Then
    assert employee_agenda.size() == (3, 2, 1)