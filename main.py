from fastapi import FastAPI,HTTPException,Path,Query
from enum import Enum
from schemas  import EnumClass,ItemClass
from typing import Annotated
 
app = FastAPI()
dummy_items = [
    {"id": 1,  "price": 1200.00},
    {"id": 1, "name": EnumClass.Mouse, "price": 25.50 , "category": [{"name": "IT Department", "register_id": 29},{"name": "IT Industory", "register_id": 19}]},
    {"id": 3, "name":  EnumClass.Keyboard, "price": 75.00},
    {"id": 4, "name":  EnumClass.Monitor, "price": 300.00},
]
# class EnumClass(Enum):
#     Laptop="laptop"
#     Mouse="mouse"
#     Keyboard="keyboard"
#     Monitor="monitor"

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "223"}

@app.get("/about")
async def about() -> str:
    return "Welcome to FAST API with python"


# Getting All Data
# @app.get("/bands")
# async def allBands() -> list[ItemClass]:
#     return [ItemClass(**item) for item in dummy_items]

# Data with Query Parameters
@app.get("/bands")
async def allBands(genere : EnumClass | None = None , has_album : bool = False ,q : Annotated[str| None, Query(max_length=10)] = None) -> list[ItemClass]:
    band_list=[ItemClass(**item) for item in dummy_items]
    if(genere!=None):
        
        band_list=[item for item in band_list if  item.name.value == genere.value]
    if(has_album!=None):
        band_list=[item for item in band_list if item.has_album == has_album]
        
    if q :
        band_list=[item for item in band_list if q.lower() in item.name.value.lower()]
    return band_list
    
   
# Data with Path Parameters

# @app.get("/bands/{band_id}")
# # async def band(band_id : int) -> list[ItemClass]:
# async def band(band_id : Annotated[int, Path(title="ID of the item to get")]) -> ItemClass:
#     band= next((item for item in dummy_items if item["id"] == band_id), None) #For one only
#     # band = [ItemClass(**item) for item in dummy_items if item["id"] == band_id] #For all
#     if(band!=None):
#         return band
#     else:
#         raise HTTPException(status_code=404, detail="Band not found")
    
    
@app.get("/bands/{band_id}")
# async def band(band_id : int) -> list[ItemClass]:
async def band(band_id : Annotated[int, Path(title="ID of the item to get")]) -> ItemClass:
    band= next((item for item in dummy_items if item["id"] == band_id), None) #For one only
    # band = [ItemClass(**item) for item in dummy_items if item["id"] == band_id] #For all
    if(band!=None):
        return band
    else:
        raise HTTPException(status_code=404, detail="Band not found")
        
    
# @app.get("/genere/{genere}")
# async def genere(genere : EnumClass) -> list[dict]:
#     # band= next((item for item in dummy_items if item["item_id"] == band_id), None) #For one only
#     band = [item for item in dummy_items if str(item["name"]).lower() == genere.value.lower()] #For all
#     if(band!=None):
#         return band
#     else:
#         raise HTTPException(status_code=404, detail="Band not found")

# Annotated Type for Data Validation + Metadata!

