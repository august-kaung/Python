x = 7
y =8
z=10

if not (x>y and x>z): print("x is greater")
    
elif(y>x and y>z): print("y is greater")
    
else: print("z is greater")

print("A") if x > y else print("B") 
    

a = 33
b = 200

if b > a: pass # no need to do anything and pass result
  

# match with if guard for doouble condition check
month = 9
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


#While looping
i = 1
while i < 6:
  print(i)
  i += 1
  if(i == 3): 
    print("connn")
  continue # break

else:
  print("i is no longer less than 6")

fruits = ['apple', 'banana', 'cherry']

#For looping
for xx in fruits:
  if xx == "banana":
    continue
  print(xx)
  
for i in range(len(fruits)):
    print(f"Index: {i}, Fruit: {fruits[i]}")

for i, fruit in enumerate(fruits, start=0):
    print(f"Position: {i}, Fruit: {fruit}")