
from typing import List

from app.domain import Employee, Job, Department


class EmployeeAgenda:
    """Models a set of employees, jobs and deparments.
    
    For each employee we have a the name, last name, hiring date, Job and Department.
    """
    
    def __init__(self):
        self._employees = {}
        self._jobs = {}
        self._departments = {}

    def _add_jobs(self, jobs: Job):
        for job in jobs:
            self._jobs[job.id] = job

    def _add_employees(self, employees: Employee):
        for employee in employees:
            self._employees[employee.id] = employee
    
    def _add_departments(self, departments: Department):
        for department in departments:
            self._departments[department.id] = department

    def get_job(self, id: int) -> Job:
        return self._jobs.get(id, None)

    def get_department(self, id: int) -> Department:
        return self._departments.get(id, None)
    
    def get_employee(self, id: int) -> Employee:
        return self._employees.get(id, None)
    
    def add_employees(self, employees: List[Employee]):
        """Adds a list of employees
        Should rollback if any of the elements cannot be added
        employees list should not contain duplicates
        """
        self._check_if_duplicate_ids(employees)
        for employee in employees:
            if self.get_employee(employee.id):
                raise ValueError(f"Employee with id {employee.id} already exists")
            
        # Check job consistency
        jobs = [employee.job for employee in employees]  
        jobs_to_be_added = []  
        for job in jobs:
            job_in_agenda = self.get_job(job.id)
            if job_in_agenda:
                if job_in_agenda != job:
                    raise ValueError(f"Job with id {job.id} already exists with different values")
            else:
                jobs_to_be_added.append(job)
        
        # Check department consistency
        departments = [employee.department for employee in employees]
        departments_to_be_added = []
        for department in departments:
            department_in_agenda = self.get_department(department.id)
            if department_in_agenda:
                if department_in_agenda != department:
                    raise ValueError(f"Department with id {department.id} already exists with different values")
            else:
                departments_to_be_added.append(department)

        self._add_jobs(jobs_to_be_added)
        self._add_departments(departments_to_be_added)
        self._add_employees(employees)      


    def _check_if_duplicate_ids(self, items: List):
        ids = [item.id for item in items]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate ids")

    def size(self) -> tuple:
        """employees, jobs, departments"""
        return len(self._employees), len(self._jobs), len(self._departments)
    
   