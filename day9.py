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
#------------------------------------------->

## EX: for loop
     #syntax: for j in rang(2,5):     
        # here j is intial variable which is defined intially
a="9"
for j in a:
    print(j)
for j in range(0,5):
     print(j)
#------------------------------------------->
 # converting string to list and tuple    
any_="str"
print(list(any_))
print(type(any_))
print(tuple(any_))
print(type(any_))     
an=[(1,3),(4,5)]
print(dict(an))
print(type(an))
#------------------------------------------->
#reverse a string 
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
#------------------------------------------->
#generating even numbers upto 100
for num in range(1,100):
    if num%2==0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")





