'''print("day7")
#getting "r" from the given list
list_1=[1,2,["python",["c",["r","Go"],"c++"],"java"],3,4]
print(list_1[2][1][1][0])
#output:"r"
#---------------------------------------
#concatination: this is nothing but ,a(+) behavior
#case1:
#integers:this will act as addition for the int
print(1+2)
#case2:
#****note: if you try to access two different data types you will get TYPE ERROR
print("str1"+"str2")
print(1+"str")#error:unsuppoted operand type (s)for + int and string
print([1,2]+"str")#error:can only concatenate list (not string) to list
#---------------------------------------
#tuple(): it is a collection of different dat types and this is represented using (),seperated by ","'''
'''
thing=(1,"kavya",[2,4],(9,6))
print(thing)
------------thing=(12,36,"pyhon",(23,"kavya",[67,"python is a language",[8,(7,8)],("python",[34,9])]))
print(thing)
print([3][2][1][9])-----------
#---------------------------------------
#swapping of two numbers
num=9
num_2=90
print(f"before swapping num={num} and num_2={num_2}")
num,num_2=num_2,num
print(f"after swapping num={num} and num_2={num_2}")
#---------------------------------------
#leap year
leap_year=int(input("enetr any year: "))
if (leap_year%4==0 and leap_year%100==0) or leap_year%400==0:
    print(f"yes,{leap_year} is a leap year")
else:
     print(f"yes,{leap_year} is not a leap year")
#---------------------------------------'''
