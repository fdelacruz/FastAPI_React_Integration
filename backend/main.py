from typing import List

from connection import Settings
import uvicorn
from beanie import PydanticObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.fruit import Fruit, FruitInResponse


# Helper function to format fruit data
def fruit_helper(fruit) -> dict:
    return {
        "id": str(fruit["_id"]),
        "name": fruit["name"],
    }


app = FastAPI()
settings = Settings()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/fruits", response_model=List[FruitInResponse])
async def get_fruits():
    fruits = await Fruit.find_all().to_list()
    # Map _id to id for the frontend
    return [fruit_helper(fruit.dict(by_alias=True)) for fruit in fruits]


@app.post("/fruits")
async def add_fruit(fruit: Fruit):
    existing_fruit = await Fruit.find_one(Fruit.name == fruit.name)
    if not existing_fruit:
        new_fruit = await fruit.create()
        return {"message": "Fruit added successfully!"}
    raise HTTPException(status_code=400, detail="Fruit already exists")

    # Format and return the response
    return fruit_helper(new_fruit.dict(by_alias=True))


@app.delete("/fruits/{id}")
async def delete_fruit(id: str):
    # Convert the string ID to PydanticObjectId
    fruit_id = PydanticObjectId(id)
    delete_fruit = await Fruit.find_one(Fruit.id == fruit_id).delete()
    if delete_fruit:
        return {"message": "Fruit deleted successfully!"}
    raise HTTPException(status_code=404, detail="Fruit not found")


@app.on_event("startup")
async def app_init():
    await settings.initialize_database()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=True)
