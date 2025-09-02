# Class Obj
class Fruit:
    id=1
    # "magic methods" or "dunder methods"
    def __init__(self, name ="Hello", color = "World"):
        self.name = name
        self.color = color
        
    # def __init__(self, name , color ):
    #     self.name = name
    #     self.color = color
    
    def __len__(self):
        return len(self.name)
    
    def myfunc(self ,address):
        print("Hello my name is " + self.name + address)

    def __str__(self):
        # if deleted safe call
        # Way - 1
        # tempColor=getattr(self,"color","deleted color")
        # return f"{self.name} is {tempColor}"
        
        # Way - 2
        if hasattr(self, 'color'):
            return f"{self.name} is {self.color}"
        else:
            return f"{self.name} has no color"
    
obj1=Fruit() 
# del obj1.color 

obj2=Fruit("grape","green")
obj2.color = "purple" 
print(f"1 is {obj1.__len__()}")
obj2.id=22222
print(f"2 is {obj1.id}")

print(f"3 is {obj1.id}")

print(f"4 is {obj1.myfunc(address="From obj1")}")
print(f"5 is {obj2.myfunc("From obj2")}")
print(f"6 is {obj1.__str__()}")

 

 
    