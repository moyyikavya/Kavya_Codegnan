#day7
vowel_con=input("enter a letter: ")
if vowel_con in "AEIOUaeiou":
    print("it is a vowel")
else:
    print("it is not a vowel")
#-----------------------------------
# converting 24 hour's clock into 12 hours clock
time_aday=input("enter 24 hours time: ")
parts_=time_aday.split(":")
hours_=int(parts_[0])
min_=int(parts_[1])
if hours_>=13 and min_<60:
    print(f"{time_aday} converted into {hours_-12}:{min_}pm")
else:
    print("you have entered normal or min are incorrect")
#LIST
#-----------------------------------
#list:different Datatypes inside the [],which are separated by, EX:[1,"name",[1,2,"kavya"]]
 
list_=[1,2,["python","java"],"language"]
str_1=list_[2]
str_2=str_1[0]
print(str_2[3])
#-----------***************
list_=[1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_[4])
print(list_[4][2])
print(list_[4][2][0])
print(list_[4][2][0][3])
#methods of list
#-----------------------------------
##1.append():this method is used to add new items into list it will only go for the last index of the list
#-----------------------------------
#syntax:variable name.append(item)
list_=[1,2,3,4,5]
print(list_)
list_.append(62)
print(list_)
#------------------------------------------
#********  mutable: i can directly modify on that particular variable
#********  immutable: i can not modify directly on the variable
#----------------------------------------
##2.extend(): this method is used to add items to list in the last index,where each item or sub string is each inex in the list.
#-----------------------------------------
list_=[1,2,3,4,5]
print(list_)
list_.extend("kavya")
print(list_)
list_1=list_.extend("kavya")
print(list_1)
#-----------------------------------------
##3.remove():this method will delete the item or a value directly 
#---------------------------------------
list_=[2,7,3,"python",4]
list_.remove(3)
print(list_)

#4.pop():it method will remove the item or value based on index number
list_=[1,2,3,4,5]
print(list_)
list_.pop(0)
print(list_)


























