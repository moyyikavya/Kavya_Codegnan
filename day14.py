#functons: function is a block of code which is reusable ,these are two types
#1. builtin or in built or pre defined function       2.user defined function
#-------built in-------> they comes program it self those are already defined.
#EX:print(),sum(),map().....etc.
#-------user defined fuctions-------> this is created by a person who is developing or using for development
# syntax: it's start with def keyword followed by function name  and it has calling function..
'''EX:def fun_name(perameters):
       block of code
       fun_name(arguments)
#--------------------------------------#even number checking
a=int(input("enter any number: "))
def even(a):#definition of the function
    if a%2==0:
        print(f"{a} is a even number")
    else:
        print(f"{a} is a odd number")              
even(a)#calling function        
#---------------------------------------------->prime num
prime_num=int(input("enter any number : "))
count=0
def prime(a,b):
    for j in range(1,a+1):
        if a%j==0:
            b+=1
    if b==0:
        print("prime")
    else:
        print("not prime")
prime(prime_num,count)
#--------------------------------------------------->fabbinacci series
a=int(input("enter range:"))
b=0
c=1
def fabbi(range_,num1,num2):
    for j in range(range_):
      range_=num1+num2
      num1=num2
      num2=range_
      print(range_)    
fabbi(a,b,c)    
#--------------------------------------------------->'''
