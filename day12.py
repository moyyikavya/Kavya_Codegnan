'''#control statements
#BREAK:this is used to exit from the loop,when we found the required valule.
for j in range(1,10):
    print(j)
    if j==5:
        break
#using list
list_=[1,2,3,4,5]
for n in list_:
    print(n)
    if n==1:
        break
#--------------------------------------------------------------------------------------------->
#continue
#using list
list_=[1,2,3,4,5]
for n in list_:
    if n==3:
        continue
    print(j)
#continue: this is used to skip the particular value and continue the rest of the remainig part
for j in range(1,10):
    if j==5:
        continue
    print(j)
#--------------------------------------------------------------------------------------------->
#pass: this is called as a place holder, incase any statement like (if,for,else, elif....)
#this should not complete'if not we will get indentation error to avoid this , 
#we use pass
#--------------------------------------------------------------------------------------------->
#else--for: it will fall back to the else block, when all loops are completed
for m in range(1,10):
    print(m)
else:
    print("else block")

#---------------------------------------------------------------------------------------------->
#while: this combination for and if statement,if we did not end the loop in proper way it will run upto the memory space becomes empty
#EX:
num = 1
while num<5:
    print(num)#it will run upto the memory space becomes empty
#----------------------------------------------------------------------------------------------->
user_in=int(input("enter the limit : "))
num1=0
num2=1
print(num1,num2,end=" ")
for v in range(user_in+1):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")'''















































