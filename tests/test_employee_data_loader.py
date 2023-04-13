
from typing import Generator, List

import pytest 

from app.loader import EmployeeAgendaDataLoader
from app.domain import Employee, Job, Department
from app.agenda import EmployeeAgenda


class EmployeeList():
    """Implementation of a data source that loads data from a list"""

    def __init__(self, employees: List) -> None:
        self._employees = employees

    def employees(self, chunk_size) -> Generator:
        """Returns an employee list generator
        Each list of employees has a maximum size of chunk_size
        """
        for i in range(0, len(self._employees), chunk_size):
            yield self._employees[i:i + chunk_size]


class MockTelemetry():
    """Mock implementation of a telemetry service"""

    def __init__(self) -> None:
        self._messages = []

    def log(self, message: str) -> None:
        self._messages.append(message)

    def get_messages(self) -> List[str]:
        return self._messages



def test_should_be_able_to_load_data_in_batch():

    # Given
    agenda = EmployeeAgenda()
    loader = EmployeeAgendaDataLoader()
    telemetry = MockTelemetry() 
    data_source = EmployeeList([
            Employee(1, "John", "Doe", "2022-12-31", Job(1, "Data Scientist"), Department(1, "Analytics")), 
            Employee(2, "Jane", "Doe", "2022-12-31", Job(2, "Software Developer"), Department(1, "Analytics")), 
            Employee(3, "Mark", "Doe", "2022-12-31", Job(3, "Project Manager"), Department(2, "Applied Research"))
        ]
    )

    # When
    loader.run(data_source, agenda, telemetry, batch_size = 2)

    # Then
    assert agenda.size() == (3, 3, 2)
    assert len(telemetry.get_messages()) == 2
    assert telemetry.get_messages()[0] == "Added employees [1, 2]"
    assert telemetry.get_messages()[1] == "Added employees [3]"
    assert agenda.get_employee(1).first_name == "John"
    assert agenda.get_employee(2).first_name == "Jane"
    assert agenda.get_employee(3).first_name == "Mark"


def test_should_rollback_and_log_if_inserting_fails_for_chunk():
    
        # Given
        agenda = EmployeeAgenda()
        loader = EmployeeAgendaDataLoader()
        telemetry = MockTelemetry() 
        data_source = EmployeeList([
                Employee(1, "John", "Doe", "2022-08-11", Job(1, "Data Scientist"), Department(1, "Analytics")), 
                Employee(2, "Jane", "Doe", "2022-09-24", Job(2, "Software Developer"), Department(1, "Analytics")),     # Duplicated ID
                Employee(2, "Mark", "Doe", "2022-12-30", Job(3, "Project Manager"), Department(2, "Applied Research")),  # Duplicated ID
                Employee(3, "Alex", "Doe", "2022-11-20", Job(3, "Project Manager"), Department(2, "Applied Research")),
                Employee(4, "Mary", "Doe", "2022-11-20", Job(3, "Project Manager"), Department(2, "Applied Research")),
            ]
        )
    
        # When
        loader.run(data_source, agenda, telemetry, batch_size = 2)
    
        # Then
        assert agenda.size() == (3, 3, 2)

        assert len(telemetry.get_messages()) == 3
        assert telemetry.get_messages()[0].startswith("Added employees [1, 2]")
        assert telemetry.get_messages()[1].startswith("Error adding employees chunk [2, 3]: ")
        assert telemetry.get_messages()[2].startswith("Added employees [4]")
        assert agenda.get_employee(1).first_name == "John"
        assert agenda.get_employee(2).first_name == "Jane"
        assert agenda.get_employee(4).first_name == "Mary" 

