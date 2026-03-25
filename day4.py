#conditional statements 
'''
if statement:this (if statement)is used to check any condition, if the condition becomes true then it will enter in the side the(if statement)
if-else statement
if-else-if statemen
#--------------------------------------------------
# example for if statement
age=int(input("enter your age:"))
if age>= 18:
        print("you are adult")
#--------------------------------------------------        
#example for if-else statement
age=int(input("Enter yiur age:"))
if age>= 18:
    print("you can vote")
else:
    print(f"you can not and have to wait {18-age} years")
    #--------------------------------------------------
#example2
    total_am = int(input("Enter the shopping money:"))
if total_am >=149:
     print("no delivery cost")
else:
    print(f"{149-total_am} to your cart")
#--------------------------------------------------
# example for if-else-if statement        
num=int(input("enter any integer from 1 to 10: "))
if num > 5:
        print(" entered number is greater than 5")
elif num < 5:
        print("entered number is less than 5")
else:
        print("entered number is equal to 5")
#--------------------------------------------------
#example2
studen_marks=int(input("Enter your marks: "))
if studen_marks >= 90:
    print("you got A+ grade")
elif studen_marks >= 75 and studen_marks <90 :
    print("you got A grade")
elif studen_marks >= 60 and studen_marks <75 :
    print("you got B+ grade")
elif studen_marks >= 50 and studen_marks <60 :
    print("you got B grade")
elif studen_marks<60 :
    print("you got c grade")
else:
    pringt("you are failed")
#--------------------------------------------------
#simple calculator
num_1=int(input("Enter any 1st integer number: "))
num_2=int(input("Enter any 2nd integer number: "))
user_choice=input("enter your choice: ")
if user_choice=="+":
    print(num_1+num_2)
elif user_choice=="-":
    print(num_1-num_2)
elif user_choice=="*":
    print(num_1*num_2)
elif user_choice=="/":
    print(num_1/num_2)
elif user_choice=="%":
    print(num_1%num_2)
else :
   print("entered choice is wrong")
#--------------------------------------------------
num_1=int(input("Enter any 1st integer number: "))
num_2=int(input("Enter any 2nd integer number: "))
user_choice=int(input("enter your choice \n1.Add \n2.Sub \n3.Mult \n4.Div :"))
if user_choice==1:
    print(num_1+num_2)
elif user_choice==2:
    print(num_1-num_2)
elif user_choice==3:
    print(num_1*num_2)
elif user_choice==4:
    print(num_1/num_2)
else:
    print("invalid choice")
#--------------------------------------------------
num=int(input("Enter any integer number: "))
if num>0:
    print("entered number is positive integer")
elif num<0:
    print("entered number is negative integer ")
else num==0:
    print(" zero is also a positive number")'''


























































