mapData ={
    "name": "John",
    "age": 36,
    "country": "Norway"
}

import json
print(json.dumps(mapData))
json_data=json.dumps(mapData)
resDict = json.loads(json_data)
print(resDict["name"])
print(resDict.get("country"))

x = 10 
try:
    if(x<10):
        raise Exception
        print(x)
except :
    print("Variable x is not defined")
else:
  print("Variable x is defined")
finally:
  print("The 'try except' is finished") 
