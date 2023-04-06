

class Job:

    def __init__(self, id: int, name: str) -> None:
        """
            Every job has an id (non negative int), a name (non empty string)
        """
        self._fail_if_id_negative(id)
        self._fail_if_empty(name)
        
        self._id = id
        self._name = name

    @staticmethod
    def _fail_if_empty(name):
        if not name.strip():
            raise ValueError("Job name cannot be empty")

    @staticmethod
    def _fail_if_id_negative(id):
        if id < 0:
            raise ValueError("Job id cannot be negative")

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    