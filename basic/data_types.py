# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType
from collections import defaultdict
# Text Type: str
string_data = "hello"
string_data_typed: str = "world"  # Type hint (Python 3.5+)

# Numeric Types: int, float, complex
int_data = 42
float_data = 3.14
complex_data = 2 + 3j

# Sequence Types: list, tuple, range
list_data = [1, 2, 3] # mutable
tuple_data = (4, 5, 6) # immutable
range_data = range(5) # need a sequence of numbers
list_data[1]=22
for i in range_data:
    print(i)

print("list_data:", list_data)
print("tuple_data:", tuple_data[2])
print("range_data:", range_data)


# Mapping Type: dict
dict_data = {"name": "John", "age": 30}
# for x in dict_data.keys():
for x in dict_data.values():
    print(x)
for k, v in dict_data.items():  #whole item 
    print(k)
print("dict_data keys:", dict_data.keys)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() # hard copy way 1

mydict = dict(thisdict) # hard copy way 2
mydict["brand"]="Suzuki"
print(mydict)
print(thisdict)

#print("dict_data:", dict_data["s"]) #Give error
print("dict_data:", dict_data.get("s")) #Safe

#return default value and also add key and value as next step
value = dict_data.setdefault("s", "Default Valuewewe")
print("dict_data:", value) 
print("Updated dict:", dict_data) 





#create defaultdict that returns sth in lambda
default_dict = defaultdict(lambda: int, dict_data)
print("default_dict:", default_dict["st"]) 
print("dict_data:", dict_data) 



# Set Types: set, frozenset (mutable vs immutable)
set_data = {1, 2, 3}
set_data.add(3)
print("set_data1:", set_data)
print("set_data2:", 22 in set_data) #in keyword
print("set_data3:", list(set_data)[1] ) # convert to list and get indexed

frozenset_data = frozenset([4, 5, 6])
frozen = frozenset([1,2,3,4])

frozen2 = frozenset([4, 5, 6, 7])

# Set operations return new frozensets
union_set = frozen.union(frozen2)
print(f"Union: {union_set}")  

intersection = frozen.intersection(frozen2)
print(f"Intersection: {intersection}")  

difference = frozen.difference(frozen2)
print(f"Difference: {difference}")   

frozenThree = set(frozen) 
frozenThree.add(7)
print("frozenset_data3:", frozenThree)


# Boolean Type: bool
bool_data = True

# Binary Types: bytes, bytearray, memoryview
bytes_data = b"hello"
bytearray_data = bytearray(1)
print("bytes_data:", bytes_data)
print("bytearray_data:", bytearray_data)
memoryview_data = memoryview(bytes_data)

b1 = bytes([65, 66, 67, 68])  
print(b1)  

b2 = b'Hello World'  
print(b2[0])   

b3 = bytes("Hello", encoding='utf-8')   
print(b3)  

# None Type: NoneType
def greet() -> int :
    print("Hello")
    return 1
result = greet()
print(result)   
print(type(result))   

# Array (same as List)
cars = ["Ford", "Volvo", "BMW"] 
print(cars[1])
cars.append("Honda")
print(cars)
cars.remove("Volvo") 
cars.pop(1) 
cars.insert(1, "Honda")
cars[2]="Tesla"
print(cars)


 