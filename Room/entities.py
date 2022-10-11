from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class User:
    name: str
    score: int


@dataclass
class MessageResponse:
    command: str
    current_users: Optional[Dict[int, User]]
    teamScores: Optional[Dict[str, int]]
    team: Optional[Any]
