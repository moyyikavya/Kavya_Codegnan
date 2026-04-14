'''#modules: module in python is simple file that cointains python code (functions, variables,classes)
------------> to use modules ,we use a keyword called import before the module
                                types of modules:
                                       |
                             ------------------------
          1.built in module or inbuilt           2. user defined module             

------------>
#<------------1.USER DEFINED MODULE----------->
#------------->this is developed by the user or a programmer inside a file or programmer inside file of python code
#------------> and used by  called import keyword  with file name
SYNTAX:import(keyword) file_name
        fileName. functionality
#-------------------------------------------------->
#Ex:
import Day1
print(Day1.add(50,20))
#---------------------BUILT IN MODULE------------------------------>
#----------->Alredy these are comes with installation and they are ready to use in the program
 import(keyword) module_name
 module_name.functionality

#EX:
import math
print(math.sqrt(4))
#Ex:
import random
input_=int(input("enter between 1 to 10 digita: " ))
rand=random.randint(1,10)
if rand==input_:
      print("you won")
else:
    print("you loss")
#---------------------------------------------------------------->
import random
attempts=3
while attempts>0:
    rand=random.randint(1,10)
    input_=int(input("enter between 1 to 10 digita: " ))
    print(rand)
    if rand==input_:
      print("you won")
    else:
        attempts-=1
print("you loss")
'''








    
