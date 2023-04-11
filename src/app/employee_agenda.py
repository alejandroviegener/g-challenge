
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

    def add_employee(self, employee: Employee):

        if employee.id in self._employees:
            raise ValueError(f"Employee with id {employee.id} already exists")
        if employee.job_id not in self._jobs:
            raise ValueError(f"Job with id {employee.job_id} does not exist")
        if employee.department_id not in self._departments:
            raise ValueError(f"Department with id {employee.department_id} does not exist")
        
        self._employees[employee.id] = employee
    
    def add_job(self, job: Job):
        if job.id in self._jobs:
            raise ValueError(f"Job with id {job.id} already exists")
        self._jobs[job.id] = job

    def get_job(self, id: int) -> Job:
        return self._jobs.get(id, None)
    
    def add_department(self, department: Department):
        if department.id in self._departments:
            raise ValueError(f"Department with id {department.id} already exists")
        self._departments[department.id] = department

    def get_department(self, id: int) -> Department:
        return self._departments.get(id, None)
    

    def add(self, employees: List, jobs: List, departments: List):
        """Adds a list of employees, jobs and departments
        Should rollback if any of the elements cannot be added
        """
        
        for job in jobs:
            if self.get_job(job.id):
                raise ValueError(f"Job with id {job.id} already exists")
        for department in departments:
            if self.get_department(department.id):
                raise ValueError(f"Department with id {department.id} already exists")
        for employee in employees:
            if self.get_employee(employee.id):
                raise ValueError(f"Employee with id {employee.id} already exists")
            if (not self.get_job(employee.job_id)) and (not employee.job_id in [job.id for job in jobs]):
                raise ValueError(f"Job with id {employee.job_id} does not exist")
            if (not self.get_department(employee.department_id)) and (not employee.department_id in [department.id for department in departments]):
                raise ValueError(f"Department with id {employee.department_id} does not exist")

        for job in jobs:
            self.add_job(job)
        for department in departments:
            self.add_department(department)
        for employee in employees:
            self.add_employee(employee)
    
    def size(self) -> tuple:
        """employees, jobs, departments"""
        return len(self._employees), len(self._jobs), len(self._departments)
    
    def get_employee(self, id: int) -> Employee:
       return self._employees.get(id, None)
    
   