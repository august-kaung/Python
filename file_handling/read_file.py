import os
import shutil
# with open("C:\\fav.txt") as f:
#     print(f.read()) 
# #  f.close()  This is for manual close
# #  print(f.readline())  line and its index's value
 
# file =  open("C:\\Users\\User\\Desktop\\favOneTwo.txt","w")  #Overwrite File From Beginning
# # file =  open("C:\\Users\\User\\Desktop\\favOneTwo.txt","a")  #Add content to File  
# file =  open("C:\\Users\\User\\Desktop\\Parent\\Child\\favOneTwo.txt","x")  #Create File  
# file.write("This is a new file by python inner child Folder line ")

file =  open("C:\\Users\\User\\Desktop\\Parent\\favOneTwo.txt")   #Read File
print(file.read()) 

# #Cant delete if open

# if os.path.exists("C:\\Users\\User\\Desktop\\favOneTwo.txt"):
#     print("The file deleted successfully")
#     os.remove("C:\\Users\\User\\Desktop\\favOneTwo.txt")
# else:
#   print("The file does not exist") 
  
#Foler Creation
# os.mkdir("C:\\Users\\User\\Desktop\\MyFolder")

# # Create nested folders (if parent doesn’t exist)
# os.makedirs("C:\\Users\\User\\Desktop\\Parent\\Child")



# Delete empty folder
# os.rmdir("C:\\Users\\User\\Desktop\\MyFolder")

# Delete folder and all contents
shutil.rmtree("C:\\Users\\User\\Desktop\\Parent\\Child")

# path = "C:\\Users\\User\\Desktop\\Parent"
# if os.path.isfile(path):
#     print("It's a file")
# elif os.path.isdir(path):
#     print("It's a folder")
    
# # path = "C:\\Users\\User\\Desktop"
# print(os.listdir(path))