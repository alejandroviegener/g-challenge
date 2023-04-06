from datetime import datetime

class Employee:

    def __init__(self, id: int, first_name: str, last_name: str, hiring_date: str, job_id: int, department_id: int):
        """
        Raises ValueError if hiring_date is not in ISO format
        Raises ValueError if id is negative
        Raises ValueError if job_id is negative
        Raises ValueError if first_name is empty
        Raises ValueError if last_name is empty
        """
        
        # Preconditions
        self._fail_if_not_iso_format(hiring_date)
        self._fail_if_negative(id)
        self._fail_if_negative(job_id)
        self._fail_if_negative(department_id)
        self._fail_if_empty_string(first_name)
        self._fail_if_empty_string(last_name)

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._hiring_date = hiring_date
        self._job_id = job_id
        self._department_id = department_id

    @property
    def hiring_date(self):
        return self._hiring_date
    
    @property
    def job_id(self):
        return self._job_id
    
    @property
    def department_id(self):
        return self._department_id

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
        
        