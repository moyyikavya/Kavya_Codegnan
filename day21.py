#OOPs
'''
-------> object-oriented programming language is a style of programming
-------->where we model real-world things as a objects that contain both data and function
--------->reusabiliy of code and also scalable and have long scope
-------->---***class***---it is a blueprint or template
-------->that defines what kind of data and behavior a certain type of object will have
--------->syn :class class_name:
                           pass
-----------> Ex:class car:
                           pass
--------->---***object***----:this is instent of a class or An object is a real instance created from class.
------------------>it is the actual thing that exist in the memory while program runs
--------->--***attribute***---:these are variables that stores the data related to the class or object
class car:
    pass
car1=car()#object1
car2=car()#object2
class dog:
    def __init__(self,breeds,color):
        self.breeds=breeds
        self.color=color
dog1=dog("bull dog"," white")    
dog2=dog("husky"," white")
print(dog1.breeds)
print(dog1.color)
#-------------------------------->
class car:
    wheels = 4
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 20
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} Miles. Total: {self.mileage}"
    def info(self):
        return f"{self.make} {self.model} {self.year}"
car1=car(make="ford",model="mustang",year="2008")
car2=car(make="toyota",model="camry",year="2023")
print(car1.info())
print(car2.info())
print(car2.drive(10))
# output:ford mustang 2008
#--------toyota camry 2023
#--------Drove 10 Miles. Total: 30
#-------------------------------->'''






    
