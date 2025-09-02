import main_module as mm
from  main_module import mapData
import datetime

print(mm.strData)
print(mm.listData)
print(mm.mapData)
print(mm.functionData2(2, 3))
print(mm.functionData())

# get all attributes from module
result = dir(mm)
print(result)
print(mapData["age"])

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%B")) 

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)    




