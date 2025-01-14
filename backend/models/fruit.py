from beanie import Document

from pydantic import BaseModel


class Fruit(Document):
    name: str

    class Settings:
        collection = (
            "fruits"  # This maps the model to the "fruits" collection in your MongoDB
        )


class FruitInResponse(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True  # Ensure it works with Beanie ORM
