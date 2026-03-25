'''#day6(data&data types)
#string :string is a collection of characters 'which is represented by double "" or triple ''' ''' qouates
str="python programming"
print(str)
#we can access the string using indexing
#-------------------------
str="python programming"
print(str[5:13])
#string is immutable,we can't able to modify it, but we can change it
#-------------------------
#replace("old string","new srting")
str="python programming"
any=str.replace("python","java")
print(any)
#string allows negative indexing
#-------------------------
str="python programming"
print(str[-1]) #ouput:g 
intro=" my name is kavya, i am from srikakulam "
#positive indexing
#-------------------------
print(f"{intro[1:17]}")
#negative indexing
print(f"{intro[-21:-1]}")
#reverse a string
#---------------------------
str="kavya"
print(str[::-1])
#finding length of string
#-------------------------
intro=" my name is kavya, i am from srikakulam "
print(len(intro))
#note: we can able to covert a string into integer if the string contain only integer values
str="123"
num=int(str)
print(type(num))
#methods of string
#-----------------
#split():, remove space and it is in the list[] it will gives the separated things in each index
#syntax:var_name.split_method("sub string")
#if you give any unknown sub string then it will execute whole string EX:str.split("   ")
str="python is a programming language"
print(str.split())
print(str.split("programming"))
#lower()
str="pytHon Is A ProgRaMmIng LangUage"
print(str.lower())
#upper()
#join()'''
str="python is a programming language"
if "is" in str:
    print("yes")
else:
    print("no")
#user entered letter if vowel or not































