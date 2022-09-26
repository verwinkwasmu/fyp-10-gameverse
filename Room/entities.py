from dataclasses import dataclass
from typing import Dict, List

@dataclass
class User:
    name: str
    score: int

@dataclass
class MessageResponse:
    command: str
    message: str
    current_users: Dict[int, User]


