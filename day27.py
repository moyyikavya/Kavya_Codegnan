'''#Error handling:
#--->try block
#--->a try block  will test a block of coad for errors
try :
    print(b)
    
#Except block
#---> this block will take care of errors
#else block
#finally block'''

try:
    a=9
    b=2
    print(a+b+c)
except:
    print("this can handle errors")
else:
    print("no errors")
finally:
    print("no try-except block is finished")
#output:this can handle errors
#       no try-except block is finished
try:
    a=9
    b=2
    print(a+b)
except:
    print("this can handle errors")
else:
    print("no errors")
finally:
    print("no try-except block is finished")
#output:11
#       no errors
#       no try-except block is finished

try:
    num1=int(input("enter any number:"))
    num2=int(input("enter any number:"))
    result=num_1/num2
except NameError:
    print("num_1 is not defined")
except ValueError:
    print("please enter valid number")
except ZeroDivisionError:
    print("can't divisible by zero")
else:
    print("no errors")
finally:
    print("no try-except block is finished")




















