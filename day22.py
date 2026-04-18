'''#constroctor(__init__): A constuctor is a special method used to initialize object data
#ex:
#--------------------------------->
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
class student:
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
    def display(self):
            print(self.name,self.ID)
student_1=student("kavya",111)
student_1.display()
#------------------------------->
#Access specifiers
#-----------------
#1.public:we can us it any where in the program
#SYN: name
#2.protected:it is only for internal views
#SYN: _name
#3.private:this one is restricted
#SYN: __name
#------------------------------------>
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
print(car2._drive(10))#protected(access modifier)
# output:ford mustang 2008
#--------toyota camry 2023
#--------Drove 10 Miles. Total: 30
#---------------------------------------->
 class some:
    def __init__(self):
        self.public="public"
        self.protected="protected"
        self.private="private"
any=some()    
print(any.public)
print(any._protected)
print(any.__private)
#------------------------------------->'''   
#self: this keyword is instance variable and unique for ecah object














































