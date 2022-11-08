from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from datetime import datetime

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
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    
