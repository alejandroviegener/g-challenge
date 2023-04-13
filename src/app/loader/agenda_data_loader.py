
from typing import Generator

from app.agenda import EmployeeAgenda


class DataSource():
    """Interface for a data source"""
    def __init__(self) -> None:
        pass

    def employees(self, chunk_size: int) -> Generator:
        """Returns an employee list generator
        Each list of employees has a maximum size of chunk_size
        """
        pass

class Telemetry():
    """Interface for a telemetry service"""
    def __init__(self) -> None:
        pass

    def log(self, message: str) -> None:
        """Logs a message"""
        pass


class EmployeeAgendaDataLoader():
    """Loads data from a DataSource into an EmployeeAgenda"""

    def __init__(self) -> None:       
        pass

    @staticmethod
    def run(data: DataSource, agenda: EmployeeAgenda, telemetry: Telemetry, batch_size = 1000) -> None:
        """Receives a EmployeeAgenda a DataSource and a Telemetry service 
        Loads the data from the DataSource into the EmployeeAgenda
        Any error is logged and the process continues
        """

        employees = data.employees(batch_size)
        for employee_chunk in employees:
            try:
                agenda.add_employees(employee_chunk)
                telemetry.log(f"Added employees {[employee.id for employee in employee_chunk]}")
            except Exception as e:
                telemetry.log(f"Error adding employees chunk {[employee.id for employee in employee_chunk]}: {e}")
