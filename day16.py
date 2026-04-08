#recursive functions
'''# recursion function is a programming techniquewhere a function calls itself either directly
or indirectly to slove a problem by breaking it into smaller, simpler subproblems.
recursion is especially usefull for problems that can be divided into identical smaller tasks, such as mathmetical, calculations,
tree traversals or divide-and-conquer algorithms.
def validate_pin(self):
    while self.remaining_attemts > 0:
        user_pin=input("enter 4 digit pin :")
        if len(user_pin) == 4 and user_pin == self.user_info['ATM PIN']:
            print("welcome to the ATM")
            return True
        else:
            self.remaining_attemts -=1
            if self.remaining_attemts > 0:
                print(f"ivalid pin.attempts left: {self.remaining_attemts} a")
            else:(f" card blocked. please contact customer care.")
            return False
#-------------------------------------------------------------------------------->
str_="  python is a language  "
vowel_list=[]
con_list=[]
def vowel_con(str_,vowel_list,con_list):
    for j in str_:
        if j in "aeiouAEIOU":
            vowel_list.append(j)
        else:
            str_.strip(" ")
            con_list.append(j)
    print(f"{vowel_list} these are all vowels in the string")        
    print(f"{con_list} these are all vowels in the string")        
vowel_con(str_,vowel_list,con_list)
#---------------------------------------------------------------------------------->
num_=int(input("Enter any number : "))
count=0
def prime_(num,count_):
    for j in range(1,num+1):
        if num % j == 0:
            count_+=1    
    if count_==2:
               print(f"-{num}- is a prime number")
    else:
               print(f"-{num}- is not a prime number.")
prime_(num_,count)
#---------------------------------------------------------------------------------->'''














