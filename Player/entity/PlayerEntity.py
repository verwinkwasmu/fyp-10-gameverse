from dataclasses import dataclass
from unicodedata import category
from sqlmodel import Column, Field, SQLModel, JSON
from typing import Dict, Optional, List
from datetime import datetime
from sqlalchemy import ARRAY, String


@dataclass
class QuizResult:
    id: int
    score: int
    category: str
    start_time: str
    end_time: str


class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(sa_column=Column("email", String, unique=True))
    total_points: int
    categories_played: Dict = Field(default={}, sa_column=Column(JSON))
    start_times: List[datetime] = Field(default=[], sa_column=Column(ARRAY(String)))
    end_times: List[datetime] = Field(default=[], sa_column=Column(ARRAY(String)))

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True

        # this prefils an example in swagger ui
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Toh Wei",
                "email": "tohwei@xiang.com",
                "total_points": 70,
                "categories_played": {
                    "Movies": {"count": 5, "points": 50},
                    "Kdrama": {"count": 2, "points": 20},
                },
            }
        }
