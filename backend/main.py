from contextlib import asynccontextmanager
from typing import List

import uvicorn
from beanie import PydanticObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from connection import Settings
from models.fruit import Fruit, FruitInResponse


# Helper function to format fruit data
def fruit_helper(fruit) -> dict:
    return {
        "id": str(fruit["_id"]),
        "name": fruit["name"],
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await settings.initialize_database()
        yield
    except Exception as e:
        print(f"Error during app initialization: {e}")
        yield  # Pass control even if there's an error


settings = Settings()
app = FastAPI(lifespan=lifespan)

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


@app.put("/fruits/{id}")
async def update_fruit(id: str, fruit: Fruit):
    fruit_id = PydanticObjectId(id)
    update_fruit = await Fruit.find_one(Fruit.id == fruit_id)
    if not update_fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")

    # Update the fruit's name
    update_fruit.name = fruit.name
    await update_fruit.save()  # Persist the changes to the database

    return {
        "message": "Fruit updated successfully!",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=True)
