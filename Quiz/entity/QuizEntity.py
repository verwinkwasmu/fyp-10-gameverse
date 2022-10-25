from sqlalchemy import ARRAY
from sqlmodel import Column, Field, SQLModel, JSON
from typing import Dict, List, Optional
from datetime import datetime


class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default=datetime.utcnow(), nullable=False)
    title: str
    category: str
    questions: List = Field(default=[], sa_column=Column(ARRAY(JSON)))
    user_id: Optional[int] = Field(default=None)

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "user_id": 1,
                "title": "Star Wars Quiz",
                "category": "Movies",
                "questions": [
                    {
                        "question": "Who is Luke's Father?",
                        "options": {
                            "option_1": "Emperor Palpatine",
                            "option_2": "Yoda",
                            "option_3": "Han Solo",
                            "option_4": "Anakin Skywalker",
                        },
                        "answer": "option_4",
                        "timer": 20,
                    }
                ],
            }
        }
