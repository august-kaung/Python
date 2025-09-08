from enum import Enum
from pydantic import BaseModel
class EnumClass(Enum):
    Laptop="laptop"
    Mouse="mouse"
    Keyboard="keyboard"
    Monitor="monitor"
    
class CategoryClass(BaseModel):
    name : str
    register_id : int
# If didn't set default value and if we didnt add data and we will get error
class ItemClass(BaseModel):
    id : int
    name : EnumClass = EnumClass.Laptop
    price : float
    category : list[CategoryClass] = []
    has_album : bool = False

