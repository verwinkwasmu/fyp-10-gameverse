from sqlalchemy import Column
from sqlmodel import ARRAY, Field, SQLModel, String
from typing import List, Optional
from datetime import datetime


class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    option_1: Optional[str] = Field(default=None, nullable=True)
    option_2: Optional[str] = Field(default=None, nullable=True)
    option_3: Optional[str] = Field(default=None, nullable=True)
    option_4: Optional[str] = Field(default=None, nullable=True)
    answer: str
    timer: int
    category: str
    created_at: Optional[datetime] = Field(default=datetime.utcnow(), nullable=False)

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Who is Luke's Father?",
                "option_1": "Emperor Palpatine",
                "option_2": "Yoda",
                "option_3": "Han Solo",
                "option_4": "Anakin Skywalker",
                "answer": "option_4",
                "timer": 20,
            }
        }
