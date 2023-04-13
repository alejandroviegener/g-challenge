


class Department: 
    """
    Department class, each department es defined by an non negative id and a name
    """
    def __init__(self, id: int, name: str) -> None:
        self._fail_if_id_negative(id)
        self._fail_if_empty(name)
        
        self._id = id
        self._name = name

    def __eq__(self, other) -> bool:
        return self.id == other.id and self.name == other.name
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @staticmethod
    def _fail_if_empty(name):
        if not name.strip():
            raise ValueError("Department name cannot be empty")

    @staticmethod
    def _fail_if_id_negative(id):
        if id < 0:
            raise ValueError("Department id cannot be negative")

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name