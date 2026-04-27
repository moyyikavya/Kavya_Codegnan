'''#Regular expression(RegEx)
---------> this regular expression or RegEx is a sequence of charecteres that forms a string pattern
--------> to use this we can use re module
functions:  1. findall
               -- >by using this function ,it will be find the all the sequence in the string
               -- > re.findall("metacharecter", var_name)
                  2.search
               -- > by using this , it will only find the first sequence  in the string
               -- >re.search("metacharecter", var_name)
                  Metacharacter:
               -- >metacharecters used to form sring pattern
                  

'''
''' :
----------------
>these are used to form searching pattern
*****1.[ ]******
     ---> This meta character we can search for [a-z],[A-Z],[0-9]
     --->
     import re
any_ ="python is programming language"
so=re.findall("[aeh]",any_)
print(so)

any_ ="python is programming language"
so=re.findall("[a-z]",any_)
print(so)
                  
any_ ="1 python is 2  programming 3 language"
so=re.findall("[123]",any_)
print(so)

any_ ="python is programming language"
so=re.findall("[ ]",any_)
print(so)

any_ ="python is programming language"
so=re.findall("[0]",any_)
print(so)

any_ ="python is programming language"
so=re.findall("[aeiouAEIOU]",any_)
print(so)

any_ ="python 2356789999 is programming 5 language"
so=re.findall("[1-9]",any_)
print(so)

******* 2.dot(.)******
     --->This meta character will form a searching pattern as it will take
          any single character for(.)
          
any_="Hola"
find=re.findall("H..a",any_)
search=re.search("H..a",any_)
print(find)
print(search)
#output:['Hola']
#           <re.Match object; span=(0, 4), match='Hola'>

****** 3. ^  ******
    ---> this is used to find the string is starting with the sequence or not
    ---> re.findall("metacharecter", var_name)

 import re
how = "hai looking gorgeous"
so = re.findall("^hai ",how)
print(so)

import re
how = "hai looking gorgeous"
so = re.search("^hai ",how)
print(so)

******  4.$ ******
    --->this is used to find the string is ending with the sequence or not
    ---> re.findall("$", var_name)

import re
how = "hai looking gorgeous jai"
so = re.findall(" jai$", how)
print(so)

import re
how = "hai looking gorgeous jai"
so = re.search(" jai$", how)
print(so)

******5.(.*)*****
   ---> this metacharecter will form a searching patterns as it will take any zero or more charecter(*)
   --->re.findall(" . * ", var_name)
   
import re
how = "hai looking gorgeous jai"
so = re.search("h.*s", how)
print(so)

***** 6.(.+) *****

import re
how = "hai looking gorgeous jai"
so = re.findall("hai.+g", how)
print(so)   




'''







