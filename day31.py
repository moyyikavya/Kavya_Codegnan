'''import re
def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email(email):
    patter = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[a-z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():
    name = input("Enter Name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    if not validate_name(name):
        print("Invalid_Name")
    elif not validate_email(email):
        print("Invalid Email")
    elif not validate_phone(phone):
       print("Invalid Phone Number")
    elif not validate password(password):
       print("Invalid Password")
    else:
        print("All inputs are valid! Form submitted successfully")
if _name_=="_main_":
    main()
#data analysis
    why this is needed ?
    this is crucial because of this will converts raw data into insitights, enableing information to make decision making easy
    and imporoves operational efficiency..
    
    1. descision macking
    2. improve operational efficiency
    3.customer understandability
    4.market insight
    5.risk management
    6. data-driven strategies (solution)


#1. lineplot
import matplotlib.pyplot as pit
x=[200,300,400,300,600]
year=[1,2,3,4,5]
pit.plot(year,x)
pit.show()

#2. Bar graph
import matplotlib.pyplot as pit
pit.bar(["TV9","NTV","SumanTv"],[4,2,1])
pit.show()

#3. Pie graph
import matplotlib.pyplot as pit
pit.pie([30,20,50],labels=["jon","jay","ashish"])
pit.show()

#4. Histograph
import matplotlib.pyplot as pit
pit.hist([30,20,50,60])
pit.show()

#NUMPY#
------> Numpy(numarical python) is the fundamental open-source liabrary for scintific computing in python,
 ----->providing high-performence, N-dimentional arrays objects (ndarray)
 ------>this enables efficient numarical compution with linear algebra,and data manipulation
-------> and also it is serving as the basis for tools like tensorflow and scipy
------>pip install nump

#array exaple
import numpy as np
arr=np.array([1,2,3])
print(arr+10)
print(arr-1)

#PANDAS#
-------> this pandas is used for handling structured data in the tabler formate
-------> pip install pandas  '''
import pandas as pd
data={"name" :["jon","jay"], "Marks" :[35,50]}
any=pd.DataFrame(data)
print(any)










    










