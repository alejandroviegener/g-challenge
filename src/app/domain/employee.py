from datetime import datetime

class Employee:

    def __init__(self, id, first_name, last_name, hiring_date):
        """
        Raises ValueError if hiring_date is not in ISO format
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


    @property
    def hiring_date(self):
        return self._hiring_date

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
        
        