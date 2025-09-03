from fastapi import FastAPI,HTTPException

app = FastAPI()
dummy_items = [
    {"item_id": 1, "name": "Laptop", "price": 1200.00},
    {"item_id": 2, "name": "Mouse", "price": 25.50},
    {"item_id": 3, "name": "Keyboard", "price": 75.00},
    {"item_id": 4, "name": "Monitor", "price": 300.00},
]
@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "223"}

@app.get("/about")
async def about() -> str:
    return "Welcome to FAST API with python"
@app.get("/bands")
async def allBands() -> list[dict]:
    return dummy_items
@app.get("/bands/{band_id}")
async def band(band_id : int) -> dict:
    band= next((item for item in dummy_items if item["item_id"] == band_id), None)
    if(band!=None):
        return band
    else:
        raise HTTPException(status_code=404, detail="Band not found")