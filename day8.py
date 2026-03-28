 #WE CAN STORE DATA AS A (KEY :VALUE)
#METHODS: 
#keys():this method is used to get all keys from the dict.
#values():this method is used to get the all values  from the dict
#clear():this method is used to delete the dict
dict_={"name":"kavya",
       "roll":"student",
       "fee":"45000"}
print(dict_.keys())
print(dict_.values())
print(dict_.clear())
#set{}: set data type is a unordered collection and it won't allow duplicates
any={1,2,3,4,4,5}
print(any)
#SET METHODS:
#union():this is used to add or get two different sets without duplicates
#intersection:this method is used to findout common items from two sets
#difference:this method is used to 
any={1,2,3,4}
so={4,5,6}
print(any.union(so))
print(any.intersection(so))
print(any.difference(so))
any.pop()
print("the removed index value :",any.pop())#it removes the 1st index value
#check weather user entered pin is write or wrong?
name_={"name":"kavya",
       "pin":"1234",
       "fee":"45000"}
pin_=input("enter your pin number")
if pin_ in name_['pin']:
     print("correct")
else:
     print("incorrect pin")





















