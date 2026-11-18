
from pathlib import Path
from model import Zone, Connection, NetworkConfig


class ParseError(Exception):
    """Raised when the map file contains invalid syntax or values."""

    def __init__(self, line_number: int, message: str) -> None:
        """Store the line number and build a readable message.

        Args:
            line_number: Line in the map file where the error occurred.
            message: Description of what is wrong.
        """
        self.line_number = line_number
        self.message = message
        super().__init__(f"Line {line_number}: {message}")

class ConfigParser:
    def __init__(self, path:str) -> None:
        self.path = path
    
    def parse(self) -> NetworkConfig:
        nb_drones: int
        start_hub: str
        end_hub: str
        hubs: list[Zone] = []
        connections: list[Connection] = []

        config_location = Path(self.path)

        with config_location.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.split("#", 1)[0].strip()

                if not line:
                    continue
                
                



        
