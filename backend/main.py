import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from models.fruit import Fruit


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
database = client.get_default_database()  # Database name
fruit_collection = database.get_collection("fruits")  # Collection name


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/fruits")
async def get_fruits():
    fruits = []
    async for fruit in fruit_collection.find():
        print("Fruit from DB:", fruit)  # Log each fruit document
        fruits.append(fruit_helper(fruit))
    print("Fruits list:", fruits)  # Log the final fruits list
    return fruits


@app.post("/fruits")
async def add_fruit(fruit: Fruit):
    existing_fruit = await fruit_collection.find_one({"name": fruit.name})
    if existing_fruit:
        raise HTTPException(status_code=400, detail="Fruit already exists")

    fruit_data = {"name": fruit.name}
    new_fruit = await fruit_collection.insert_one(fruit_data)
    created_fruit = await fruit_collection.find_one({"_id": new_fruit.inserted_id})
    return fruit_helper(created_fruit)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001, reload=True)
