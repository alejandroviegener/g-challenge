from datetime import datetime

from .department import Department
from .job import Job

class Employee:

    def __init__(self, id: int, first_name: str, last_name: str, hiring_date: str, job: Job, department: Department):
        """
        Raises ValueError if hiring_date is not in ISO format
        Raises ValueError if id is negative
        Raises ValueError if first_name is empty
        Raises ValueError if last_name is empty
        """
        
        # Preconditions
        self._fail_if_not_iso_format(hiring_date)
        self._fail_if_negative(id)
        self._fail_if_empty_string(first_name)
        self._fail_if_empty_string(last_name)

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._hiring_date = hiring_date
        self._job = job
        self._department = department

    @property
    def hiring_date(self):
        return self._hiring_date
    
    @property
    def job(self):
        return self._job
    
    @property
    def department(self):
        return self._department

    @staticmethod
    def _fail_if_not_iso_format(hiring_date: str) -> None:
        """Check if hiring_date is in ISO format YYYY-MM-DD, with no time component"""
        try:
            datetime.strptime(hiring_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Date {hiring_date} not in iso format YYYY-MM-DD")
        
    @staticmethod
    def _fail_if_negative(id: int) -> None:
        """Check if id is negative"""
        if id < 0:
            raise ValueError(f"Id must be positive, not {id}")
    
    @staticmethod
    def _fail_if_empty_string(name: str) -> None:
        """Check if string is empty"""
        if name.strip() == "":
            raise ValueError(f"Empty string")
        
        