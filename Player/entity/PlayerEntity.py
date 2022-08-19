from sqlmodel import Column, Field, SQLModel, JSON
from typing import Dict, Optional


class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    total_points: int
    # category_points: Dict = Field(default={}, sa_column=Column(JSON))
    categories_played: Dict = Field(default={}, sa_column=Column(JSON))

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True

        # this prefils an example in swagger ui
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Toh Wei",
                "email": "tohwei@xiang.com",
                "categories_played": {
                    "Movies": {"count": 5, "points": 50},
                    "Kdrama": {"count": 2, "points": 20},
                },
            }
        }
