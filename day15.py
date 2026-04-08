'''#ways to pass arguments in calling function
required arguments
it should match same number of variables in calling function with the definition or arguments with perameters

num_1 = 10
num_2 = 10
def add(num1,num2):
    print(num1+num2)
add(num_1,num_2)    
#---------------------------------------------------------------->
my_name="kavya"
def add(my_name):
    print(my_name)
add(my_name="kavya moyyi")
add(my_name="anil mpyyi")
add(my_name="anu moyyi")
add(my_name="simha moyyi")
#---------------------------------------------------------------->
#checking prime number
#num_=int(input("enter any number : "))
num=7
count=0
def prime(num,count):
    for j in range(1,num+1):
        if num%j==0:
            count+=1
    if count== 2:
        print(f"-{num}- is a prime number")
    else:
        print(f"-{num}- is not a prime number")
prime(num=4, count=0)
prime(num=10, count=0)
#--------------------------------------------------------------->
def name(*candidate_):
     print(candidate_)
name("kavya", "vasavi")     
#variable length arguments: adding a star * before the perameter name in the function receivs a tuple of arguments
#--------------------------------------------------------------->'''

