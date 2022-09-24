from sqlalchemy import Column
from sqlmodel import ARRAY, Field, SQLModel, String
from typing import List, Optional


class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    option_1: str
    option_2: str
    option_3: str
    option_4: str
    answer: List = Field(default=[], sa_column=Column(ARRAY(String)))
    timer: int
    category: str

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
                "answer": "Anakin Skywalker",
                "timer": 20,
            }
        }