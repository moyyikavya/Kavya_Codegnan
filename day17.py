#lambda function

'''----> this also called anonymous function..
   ----> a lambda function can take n number of arguments but have only one expression
   ---->syntax: lambda (keyword) arguments :expression
any = lambda so : so + 10
print(any(6))

#------------------------------>

any = lambda so,that : that-so
print(any(6,10))

#------------------------------>multiplication<----

some=lambda so,any_,how: (any_-so)* how
print(some(10,20,10))

#------------------------------>division<----------

some=lambda so,any_,how: (any_-so)/ how
print(some(10,20,10))
#o/p:1.0
#note: by deafult output is in float form

#------------------------------>modulous<----------

some=lambda so,any_,how: (any_-so)% how
print(some(10,20,10))
#o/p:0

#------------------------------>addition<----------

some=lambda so,any_,how: (any_-so)+ how
print(some(10,20,10))
#o/p:20

#------------------------------>subtraction<-------

some=lambda so,any_,how: (any_-so)- how
print(some(10,20,10))
#o/p:0

#------------------------------>

num1=int(input("enter any number:"))
so=int(input("enter any number:"))
any = lambda so : so + num1
print(any(so))

#------------------------------>

#---------->LIST COMPREHENSION: this is offers the shorter syntax
#---------->when you want to create a new list from the existing list
#---------->syntax: var_name = [expression loop and addition ] 
#EX:
old_list=[1,2,3,4,5]
new_list=[j for j in old_list if j%2==0]
print(new_list)

#----------------------------->

old_list=[1,2,3,4,5]
new_list=[j for j in old_list ]
print(new_list)

#------------------------------>'''
























