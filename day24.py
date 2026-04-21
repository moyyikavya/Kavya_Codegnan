'''#mulilevel inheritance:
----------> this occurs when a class inherit from a child class
----------> creating a grandparant--> parant-->child
class grandParent:
    def show_GP(self):
        print("I'm grand parent")
class Parent(grandParent):
    def show_P(self):
        print("I'm parent")
class child(Parent):
    def show_ch(self):
        print("I'm child")
obj=child()
obj.show_GP()
obj.show_P()
obj.show_ch()
#--------------------------------->
class Area:    
    def __init__(self,length,breath,height):
           self.length=length
           self.breath=breath
           self.height=height
class Area_rectangle(Area):
    def rectangle(self):
        print(self.length*self.breath*self.height)
class Area_square(Area_rectangle):
    def square(self):
        print(self.length*self.breath)
obj=Area_square(2,4,5)
obj.square()
obj.rectangle()
#--------------------------------------->
#hierarchical:this occurs when multiple child classes iinherit from the single parant class
#-------------> this process is called hierarchical inheritance
class parent:
    def parent(self):
        print("Im a parent")
class child_1(parent):
    def child_(self):
        print("im 1st child")
class child_2(parent):
    def _child(self):
        print("im 2nd child")
class child_3(child_1, child_2):
    def child(self):
        print("im  child")
thing = child_3()
thing.parent()
thing.child_()
thing._child()
thing.child()
#-------------------------------------->
#hybrid inheritance: this is combination of two or more inheritance , such as single ,        
#-------------> multiple,multi level, or hierarchical all this in a single class                    

class grandParent:
    def show_GP(self):
        print("I'm grand parent")
class Parent(grandParent):
    def show_P(self):
        print("I'm parent")
class child(Parent):
    def show_ch(self):
        print("I'm child")

class parent:
    def parent(self):
        print("Im a parent")
class child_1(parent):
    def child_(self):
        print("im 1st child")
class child_2(parent):
    def _child(self):
        print("im 2nd child")
class child_3(child_1, child_2,grandParent):
    def child(self):
        print("im  inherited from grand parant class and child_1,child_2")
thing = child_3()
thing.parent()
thing.show_GP()
thing._child()
thing.child()
#------------------------------------------------------->'''









