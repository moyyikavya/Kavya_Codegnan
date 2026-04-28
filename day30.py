'''#7.
#_____.?______
#---->this meta charecter will form a searching pattern as it will take any zero or oe charecter for (?)
#syn:   re.findall("th.?",Var_name)
import re
any_="this meta charecter will form a searching pattern as it will take any zero or one charecter for (?)"
an=re.findall("th.?",any_)
print(an)
any_="this meta charecter will form a searching pattern as it will take any zero or one charecter for (?)"
an=re.search("th.?",any_)
print(an)
#8.
#____.{}_____
#---->="this meta charecter will form a searching pattern as we can mention the size in the curlybrackets{}
#syn:re.findall(".{size}",Var_name)
any_="this meta charecter will form a searching pattern as it will take any zero or one charecter for (?)"
an=re.findall(".{25}it",any_)
print(an)

any_="this meta charecter will form a searching pattern as it will take any zero or one charecter for (?)"
an=re.findall(".{25}",any_)
print(an)
#9.
#____
#--. this meta charecter will form as searching pattern as it considered ringht or left any string is present or not for (|)
any_="this meta charecter will form a searching pattern as it will take any zero or one charecter for (?)"
an=re.findall("that|will",any_)
print(an)

#Special sequaence
#1.______\A________
#returns a match if the specified charecters are at the beggining of the string
any_="this meta charecter will form a searching pattern as it will take any zero or one charecter for (?)"
an=re.findall("\Athis",any_)
print(an)
if an:
    print("yes, there is a match")
else:
    print("no match")

#2:\b- Returns a match where the specified characters are at the beginning or at  
#         end of a word  
# Eg: r"\bain"
 
import re
txt = "The rain in Spain"
 #Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
#3:\d
import re
txt = "The rain in  111 Spain"
#check if the string contains any digits (number fron 0-9)
x = re.findall(r"\d", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
#4:\D- Returns a match where the string DOES NOT contain digits
#Eg: "\D"
import re
txt = "The rain in 67 Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#\s- Returns a match where the string contains a white space
#character
#Eg: "\s"
import re
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#\S- Returns a match at every NON white-space charecter:
#character
#Eg: "\s"
import re
txt = "The rain in Spain"
#Return a match at every non white-space character:
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
_____________________________________
#TIME AND DATE
%d----->day
%m---->month
%y----->year
%H----->Hour
%M----->minuts
%S------>sec
%p----->AM/PM
%A----->Day name
%B------>Month name
'''
import datetime
now=datetime.datetime.now()
print(now)

import datetime
today=datetime.date.today()
print(today.strftime("%d-%m-%y"))
print(today.strftime("%A"))
print(today.strftime("%B"))


























