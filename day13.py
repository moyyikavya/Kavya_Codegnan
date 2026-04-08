#
num=int(input("enter the limit   :"))
for j in range(num):
    for i in range(1,j):
        print("*",end = " ")
    print()
    '''
#--------------------------------------------------------------------------------------------->   
#square
num=int(input("enter the limit   :"))
for j in range(num):
    for i in range(num):
            print("*",end="")
    print()
#uotpu:enter the limit   :5
#    *****
#    *****
#    *****
#    *****
#    *****    
#-------------------------------------------------------------------------------------------->
num=int(input("enter the limit   :"))       
for j in range(num):
    for i in range(num-j):
        print("*",end = " ")
    print()
#output:enter the limit   :5
#   * * * * * 
#   * * * * 
#   * * * 
#   * * 
#   *     
#--------------------------------------------------------------------------------------------->   
num=int(input("enter the limit   :"))
for j in range(num):
    print(" "*(num-j),end="")
    for i in range(j+1):
        print("*",end=" ")
    print()    
#OUTPUT:
#enter the limit   :5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#--------------------------------------------------------------------------------------------->'''
num=int(input("enter the limit   :"))
for j in range(num):
    print(" "*(num-j),end="")
    for i in range(j+1):
        print("*",end=" ")  


































                   
