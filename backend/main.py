from typing import List

import uvicorn
from beanie import PydanticObjectId, init_beanie
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from models.fruit import Fruit, FruitInResponse


# Helper function to format fruit data
def fruit_helper(fruit) -> dict:
    return {
        "id": str(fruit["_id"]),
        "name": fruit["name"],
    }


app = FastAPI()

# MongoDB connection details
MONGO_DETAILS = "mongodb://root:rootroot@mongodb:27017/fruits_db?authSource=admin"
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.get_default_database()  # Database name


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
    return [{"id": str(fruit.id), "name": fruit.name} for fruit in fruits]


@app.post("/fruits")
async def add_fruit(fruit: Fruit):
    existing_fruit = await Fruit.find_one(Fruit.name == fruit.name)
    if existing_fruit:
        raise HTTPException(status_code=400, detail="Fruit already exists")

    # Save the new fruit using Beanie's `create` method
    # try:
    #     new_fruit = await fruit.create()
    #     return fruit_helper(new_fruit)
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=f"Error adding fruit: {str(e)}")
    # Insert the fruit into the database
    new_fruit = await fruit.create()

    # Format and return the response
    return {
        "id": str(new_fruit.id),  # Convert ObjectId to string
        "name": new_fruit.name,
    }


@app.delete("/fruits/{id}")
async def delete_fruit(id: str):
    try:
        # Convert the string ID to PydanticObjectId
        fruit_id = PydanticObjectId(id)
        result = await Fruit.find_one(Fruit.id == fruit_id).delete()
        if result:
            return {"message": "Fruit deleted successfully"}
        raise HTTPException(status_code=404, detail="Fruit not found")
    except Exception as e:
        print("Error deleting fruit:", e)  # Log the error for debugging
        raise HTTPException(status_code=400, detail="Invalid ID format")


@app.on_event("startup")
async def app_init():
    # Initialize Beanie with the MongoDB connection and models
    await init_beanie(database=db, document_models=[Fruit])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=True)
