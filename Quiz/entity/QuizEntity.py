from sqlmodel import Column, Field, SQLModel, JSON
from typing import Dict, Optional


class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    category: str
    questions: Dict = Field(default={}, sa_column=Column(JSON))

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Star Wars Quiz",
                "category": "Movies",
                "questions": {
                    "question_1" : {
                        "question" : "Who is Luke's Father?",
                        "option_1": "Emperor Palpatine",
                        "option_2": "Yoda",
                        "option_3": "Han Solo",
                        "option_4": "Chewbacca",
                        "answer": "Anakin Skywalker"
                    }
                },
            }
        }
