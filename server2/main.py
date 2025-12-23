from fastapi import FastAPI
import uvicorn
from pathlib import Path
import json
from pydantic import BaseModel
from typing import Optional, Dict


app = FastAPI()

DB_PATH = Path("db/shopping_list.json")
DB_PATH1 = Path("data/backup_shopping_list.json")


class Item(BaseModel):
    id:int
    name: str
    quantity: int

def check_database_exists() -> None:
    if not DB_PATH.exists():
        print(f"ERROR: Database file not found at {DB_PATH}")
        print("In development: Create the data/db.json file manually")
        print("In Docker: Mount a volume to /app/data with the db.json file")
        raise FileNotFoundError(f"Database file not found: {DB_PATH}")

def load_database():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def load_database1():
    with open(DB_PATH1, "r") as f:
        return json.load(f)

@app.get("/items")
def to_list():
    return load_database()

@app.post("/items")
def add(item: Item):
    
     return {
            "id": 
            "name":
            "quantity":
            }

@app.get("/backup")   
def to_list1():
    return load_database1()

@app.post("/backup/save")
    return


if __name__ == "__main__":
    check_database_exists()
    uvicorn.run(app, host="0.0.0.0", port=8000)
