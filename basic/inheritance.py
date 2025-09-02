class Person :
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print(self.firstname, self.lastname)
        
class Student(Person):
    pass
# person=Person("Kaung","Htet")
student1=Student("Hsu","Htet")

class Work :
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print(self.firstname, self.lastname)
        
class Human(Work):
    location = "Yangon"
    def __init__(self, fname, lname ,loc):
        self.location = loc
        super().__init__(fname, lname)
        print(self.location)
 
human1=Human("Doctor","Engineer","Myaung Mya")
 