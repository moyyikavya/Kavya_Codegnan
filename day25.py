'''#polymorphism :
--> this allows an object of different classes to be treated as instance
->of same base class , with methods behaving differently based on the actual objects type
#EX:
print(len("python"))
print(len([1,2,3]))
#method over loading :
#-------------> thlis defines multiple methods with same name but with different parameters
#-------->(number,type, or order) in the same class
class calculator:
    def add(self,a=0,b=0,c=0):
        return a-b+c
cal=calculator()
print(cal.add(2))
print(cal.add(2,3))
print(cal.add(2,3,4))
#method overriding:
#------------> this occurs in the child class, redefining a parent class method with the same signature for runtime
import pyttsx3
engine = pyttsx3.init()
class animal:
    def speak(self):
        return "sound"
class dog(animal):
    def speak(self):
        return "woof"
class cat(animal):
    def speak(self):
        return "meow"
class snake(animal):
    def speak(self):
        return "shuuuuu"
dog_=dog()
s=dog_.speak()
engine.say(s)
print(s)
engine.runAndWait()

#---------------------------------->
class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return someone(self.a+other.a,self.b+other.b)
    def __str__(self):
        return f"{self.a} ,{self.b}"
Any=someone(2,3)
so=someone(5,20)
print(Any+so)
#------------------------------------->
#Data abstraction:
#----------> this hides the complex implimentation details, exposing only essential
#---------->features via abstract class or interface.
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
Circle = circle(4)
print(Circle.area())


'''














