'''#generators:
----------->this is a special type of function that returns an ITERATOR which one at a time
   #yield:
----------->  It will take a pasue and again res,this is not a normal keyword  can not be used in the normal function 
----------->  This is used to produse a value and pause execution
   #Next():
----------->  This is used to get next value from generator
#---------->  When the value is finshed , it will stop the iterator
#---------------------------------------------------------------------------->
def generator():
    yield 1
    yield 2
    yield 3
an=generator()
print(next(an))
print(next(an))
print(next(an))
#---------------------------------------------------------------------------->   
def square(n):
    for i in range(n):
        yield i*i
for val in square(30):
    print(val)
#---------------------------------------------------------------------------->    
def even(n):
    for i in range(n):
        if i%2==0:
            yield i
for val in even(20):
    print(val)
#---------------------------------------------------------------------------->
def cube(n):
    for i in range(n):
        yield i*i*i
for val in cube(30):
    print(val)
#---------------------------------------------------------------------------->'''

    


























