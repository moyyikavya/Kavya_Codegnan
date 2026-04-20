'''#encapsulation:
#------>  the pricnciple of bounding data( attributes) and methods 
#          that operate on that data into a single unit, which is a class
class bankAC:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
ACC=bankAC(15000)
ACC.deposite(7000)
print(ACC.get_balance())
#--------------------------->
inheritance:
----> this allows a child class (sub calss) to acquire the attributes or methods of a parant class(base class)
this is called inheritance
___________________________________________

1.single level:
--------------> using single method of the class from parant class is known as single inheritance
class parant:
    def display(self):
        print("this is parant method")
class child(parant):
    def display(self):
        super().display()
        print("this is child method")
obj=child()
obj.display()
_________________________________________
#2. multi level:
---------------> A child class inherit
class father:
    def skills_1(self):
        print("Father : hard workig")
class mother:
    def skills_2(self):
        print("Mother : cooking")
class child(father, mother):
    def all_skills(self):
        print("Child  : coding")
obj=child()
obj.skills_1()
obj.skills_2()
obj.all_skills()    

#super(): this is used to call methods of parant class from the child class
#__________________________________________'''
















