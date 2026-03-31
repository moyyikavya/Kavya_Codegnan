'''# checking prime numbers
prime_num=int(input("enter any integer number: "))
count=0
for j in range(1,prime_num):
    if prime_num % j == 0:
        count += 1
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")
#------------------------------------------------------------------>
#generate prime numbers certain range
for an in range(2,100):
    count=0
    for j in range(1,an+1):
        if an % j==0:
            count+=1
    if count == 2:
           print(f"{an} is a prime number")
    else:
           print(f"{an} is not a prime number")            
#list-------------------------------------------------------------->
list_=[1052,197,9,17673,86]
for an in list_:
    count=0
    for j in range(1,an+1):
        if an % j==0:
            count+=1
    if count == 2:
            print(f"{an} is a prime number")
    else:
            print(f"{an} is not a prime number")         
#------------------------------------------------------------------->    
#removing duplicates
any_=[2,356,8,6,3,2,8]
empty_=[]
for j in any_:
    if j not in empty_:
        empty_.append(j)
        print(empty_)
#------------------------------------------------------------------->
#checking armstrong numbers
so=int(input("enter a number :"))
length_=len(str(so))       
armstr_=0
for j in str(so):
            armstr_+=int(j) ** length_
            print(armstr_)
if armstr_==so:
            print(f"{so} is a armstrong number")
else:
            print(f"{so} is a armstrong number")'''























