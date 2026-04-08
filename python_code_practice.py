'''#Q1:counting number of vowels,consonents,spaces in a paragraph
count_space=0
count_vowel=0
count_consonent=0
paragraph="counting number of vowels,consonents,spaces in a paragraph"
len_=len(paragraph)
print("length of the given paragraph: ",len_)
for j in paragraph:
    if j in " ":
        count_space+=1    
print(f"number of spaces are :{count_space}")
for j in paragraph:
    if j in "AEIOUaeiou":
        count_vowel+=1
print(f"number of vowels are :{count_vowel}")
sum_=count_space+count_vowel        
print("number of consonents are:",len_-sum_)
#--------------------------------------------------------------------------->
#Q2)#reverse a string 
name="kavya"
print(name[::-1])

#reverse a string withot using ::-1

rev_str="kavya"
empty_=""
for j in rev_str:
    empty_=j+empty_  # it performs concatination
    print(empty_)
if rev_str==empty_:
    print("it is a palindrome")
else:
    print("it is not palindrom")
#method 2:
paragraph="counting number of vowels,consonents,spaces in a paragraph"
count_space=0
count_vowel=0
count_consonent=0
for j in paragraph:   
    if j in " ":       
          count_space+=1
    elif j in "AEIOUaeiou":
          count_vowel+=1
print(f"length of the spaces

#--------------------------------------------------------------------------->
#generating even numbers upto 100
for num in range(1,100):
    if num%2==0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")
#------------------------------------->
for num in range(1,100):
    if num%2==0:
        print(f"{num} is a even number")
else:
        print(f"{num} is a odd number")
 #checking prime numbers
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
#------------------------------------------------------------------->'''
#take a list only with integers and add odd and even numbers separat     


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
#----------------------------------------------------------------------------->
#Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
count_ = fruits.count("cherry")
print(count_)  #output:1
#Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("jhon","Peter", "Vicky")
x = "#".join(myTuple)
print(x) #output:jhon#peter#vicky                 
#-------------------------------------------------------------------------->
#Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
#-------------------------------------------------------------------------->
#Replace the word "bananas":
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#-------------------------------------------------------------------------->
#Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)  #output:['welcome', 'to', 'the', 'jungle']
#-------------------------------------------------------------------------->
#Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x) #output:Hello, and welcome to my world.
#-------------------------------------------------------------------------->
#Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)  #output: hello, and welcome to my world!
#-------------------------------------------------------------------------->
#Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)  #output:true
#-------------------------------------------------------------------------->
#Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x) #output:true
#-------------------------------------------------------------------------->
#other methods
#isdigit()
#isdecimal()
#islower()
#isupper()

#list methods
#A list in Python is a collection of items stored in a single variable.



# Create a list
nums = [10, 20, 30]

print("Original list:", nums)

# ----------- Adding elements -----------
nums.append(40)        # adds element at end
print("Append:", nums)

nums.insert(1, 15)     # inserts 15 at index 1
print("Insert:", nums)

nums.extend([50, 60])  # adds multiple elements
print("Extend:", nums)

# ----------- Removing elements -----------
nums.remove(20)        # removes specific value
print("Remove:", nums)

nums.pop()             # removes last element
print("Pop last:", nums)

nums.pop(1)            # removes element at index 1
print("Pop index 1:", nums)

# ----------- Searching -----------
print("Index of 30:", nums.index(30))  # finds index of element
print("Count of 10:", nums.count(10))  # counts occurrences

# ----------- Sorting & reversing -----------
nums.sort()            # sorts list in ascending order
print("Sorted:", nums)

nums.reverse()         # reverses list
print("Reversed:", nums)

# ----------- Copying -----------
new_list = nums.copy() # creates a copy of list
print("Copied list:", new_list)

# ----------- Clearing -----------
nums.clear()           # removes all elements
print("Cleared list:", nums)
#------------------------------------------------------------------------------>'''
# checking user enterd in is valid or ivalid
icic_kav_ac_details={"name":"kavya",
                     "ATM PIN":"1111",
                     "balance":5000}
print("welcome to icic ATM")
print("please enter your ATM card")
icic_user_pin=input("please enter your 4 digit ATM PIN number :")
if len(icic_user_pin)==4:
    if icic_user_pin in icic_kav_ac_details['ATM PIN']:
        user_choice_=int(input("\n1.withdraw :"))
        if user_choice_==1:
            money_w=int(input(" enter amount you want to withdraw :"))
            if money_w<icic_kav_ac_details['balance']:
                if
            else:
                    print("insuff")                                    
     print("the pin is correct")
    else:
        print("you have entered ivalid pin number")
else:
    print("please enter 4 digit pin")
    












    
