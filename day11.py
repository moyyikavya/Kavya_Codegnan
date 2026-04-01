'''#printig table:
table_num=int(input("enter a number :"))
for j in range(1,11):
    print(f"{table_num} X {j} = {table_num*j}")
#----------------------------------------------------------------------------->    
str_=" Rid Explore Be your self "
count_u=0
count_l=0
for cap in str_:
    if cap.isupper():
        count_u+=1
    elif cap.islower():
         count_l+=1
print(f"there are total {count_u} capital letters")
print(f"there are total {count_l} small letters")
#----------------------------------------------------------------------------->
str_=" Rid Explore Be your self "
_cap=[]
_small=[]
for st_ in str_:
    if st_.isupper():
        _cap.append(st_)
    elif st_.isupper():
         _small.append(st_)
print(f"{_cap}")         
print(f"{_small}")         
#----------------------------------------------------------------------------->        
# checking user enterd in is valid or ivalid
icic_kav_ac_details={"name":"kavya",
                     "ATM PIN":"1111"}
print("welcome to icic ATM")
print("please enter your ATM card")
icic_user_pin=input("please enter your 4 digit ATM PIN number :")
if len(icic_user_pin)==4:
    if icic_user_pin in icic_kav_ac_details['ATM PIN']:
        print("the pin is correct")
    else:
        print("you have entered ivalid pin number")
else:
    print("please enter 4 digit pin")
#----------------------------------------------------------------------------->
# checking perfect number
per_num=int(input("enter any number :"))
factor_all=0
for j in range(1,per_num):
            if per_num%j==0:
                 factor_all+=j
if factor_all == per_num:
    print(f"{per_num} is a perfect number")
else:
    print(f"{per_num} is not a perfect number")
#----------------------------------------------------------------------------->'''
























    
