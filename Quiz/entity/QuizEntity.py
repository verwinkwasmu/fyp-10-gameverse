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