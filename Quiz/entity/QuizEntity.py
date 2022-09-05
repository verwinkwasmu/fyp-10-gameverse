from sqlalchemy import ARRAY
from sqlmodel import Column, Field, SQLModel, JSON
from typing import Dict, List, Optional


class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    category: str
    # questions: Dict = Field(default={}, sa_column=Column(JSON))
    questions: List = Field(default=[], sa_column=Column(ARRAY(JSON)))

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Star Wars Quiz",
                "category": "Movies",
                "questions": [
                    {
                        "question": "Who is Luke's Father?",
                        "option_1": "Emperor Palpatine",
                        "option_2": "Yoda",
                        "option_3": "Han Solo",
                        "option_4": "Anakin Skywalker",
                        "answer": "Anakin Skywalker",
                        "timer": 20,

                    }
                ],
            }
        }
