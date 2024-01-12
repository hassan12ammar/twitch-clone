# import files
from dataclasses import dataclass

@dataclass
class Error:
    status: int
    message: str

    def __str__(self) -> str:
        return f"{self.status}: {self.message}"

