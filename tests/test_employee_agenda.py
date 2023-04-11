
from typing import List

import pytest

from app.domain import Employee, Job, Department
from app.employee_agenda import EmployeeAgenda

def test_should_be_able_to_add_new_employee_if_job_and_department_present():

    # Given
    jobs = [Job(2, "Software Engineer")]
    departments = [Department(3, "IT")]
    employee_agenda = prepare_agenda_with(jobs, departments)

    # When
    employee = Employee(1, "John", "Doe", hiring_date="2022-12-31", job_id=2, department_id=3)
    employee_agenda.add_employee(employee)

    # Then
    assert employee_agenda.get_employee(1) == employee


def test_should_fail_if_adding_employee_with_existing_id():

    # Given
    jobs = [Job(2, "Software Engineer")]
    departments = [Department(3, "IT")]
    employee_agenda = prepare_agenda_with(jobs, departments)


    # When
    original_employee = Employee(1, "John", "Doe", "2022-12-31", 2, 3)
    employee_agenda.add_employee(original_employee)
    
    # Then
    with pytest.raises(ValueError):
        employee = Employee(1, "NoJohn", "NoDoe", "2022-12-31", 3, 4)
        employee_agenda.add_employee(employee)

    assert employee_agenda.get_employee(1) == original_employee


def test_should_fail_if_adding_employee_with_not_added_job():

    # Given
    departments = [Department(3, "IT")]
    employee_agenda = prepare_agenda_with([], departments)
    employee = Employee(1, "John", "Doe", "2022-12-31", 2, 3)

    # Then
    with pytest.raises(ValueError):
        employee_agenda.add_employee(employee)


def test_should_fail_if_adding_employee_with_not_added_department():
   
    # Given
    jobs = [Job(2, "Software Engineer")]
    employee_agenda = prepare_agenda_with(jobs, [])

    # Then
    with pytest.raises(ValueError):
        employee = Employee(1, "John", "Doe", "2022-12-31", 2, 3)
        employee_agenda.add_employee(employee)


def test_should_fail_if_adding_job_with_existing_id():
    
    # Given
    original_job = Job(2, "Software Engineer")
    employee_agenda = prepare_agenda_with([original_job], [])

    # Then
    with pytest.raises(ValueError):
        job = Job(2, "Software Engineer 2")
        employee_agenda.add_job(job)

    assert employee_agenda.get_job(2) == original_job


def test_should_fail_if_adding_department_with_existing_id():

    # Given
    original_department = Department(3, "IT")
    employee_agenda = prepare_agenda_with([], [original_department])

    # Then
    with pytest.raises(ValueError):
        department = Department(3, "IT 2")
        employee_agenda.add_department(department)

    assert employee_agenda.get_department(3) == original_department


def test_should_be_able_to_add_registers_in_batch_in_empty_agenda():

    # Given
    jobs = [Job(2, "Software Engineer"), Job(3, "Data Engineer"), Job(4, "Data Scientist")]
    departments = [Department(3, "IT"), Department(4, "IT 2")]
    employees = [Employee(1, "John", "Doe", "2022-12-31", 2, 3), Employee(2, "Jane", "Doe", "2022-12-31", 3, 4)]

    # When
    employee_agenda = EmployeeAgenda()
    employee_agenda.add(employees, jobs, departments)

    # Then
    assert employee_agenda.size() == (2, 3, 2)


def test_should_be_able_to_add_employees_in_batch_if_jobs_and_departments_already_inserted():
    
    # Given
    jobs = [Job(1, "Software Engineer"), Job(2, "Data Engineer"), Job(3, "Data Scientist")]
    departments = [Department(1, "IT"), Department(2, "Machine Learning")]
    employee_agenda = prepare_agenda_with(jobs, departments)

    # When
    new_employees = [Employee(1, "John", "Doe", "2022-12-31", 1, 1), Employee(2, "Jane", "Doe", "2022-12-31", 2, 2), Employee(3, "John", "Doe", "2022-12-31", 3, 3)]
    new_departments = [ Department(3, "Analytics")]
    employee_agenda.add(new_employees, [], new_departments)

    # Then
    assert employee_agenda.size() == (3, 3, 3)


def test_batch_add_transaction_should_rollback_if_it_fails():
    """
    Test that the batch transaction is rolled back if it fails
    """
        
    # Given
    jobs = [Job(1, "Software Engineer"), Job(2, "Data Engineer"), Job(3, "Data Scientist")]
    departments = [Department(1, "IT"), Department(2, "Machine Learning")]
    employee_agenda = prepare_agenda_with(jobs, departments)

    # When
    employees = [Employee(1, "John", "Doe", "2022-12-31", 1, 1), Employee(2, "Jane", "Doe", "2022-12-31", 2, 2), Employee(3, "John", "Doe", "2022-12-31", 3, 3)]

    # Then
    with pytest.raises(ValueError):
        employee_agenda.add(employees=employees, jobs=[], departments=[])

    assert employee_agenda.size() == (0, 3, 2)


################################################################################################ 


def prepare_agenda_with(jobs: List[Job], departments: List[Department]) -> EmployeeAgenda:
    agenda = EmployeeAgenda()
    for job in jobs:
        agenda.add_job(job)
    for department in departments:
        agenda.add_department(department)
    return agenda