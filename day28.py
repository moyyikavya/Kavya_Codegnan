'''#file  handling
--> file handler is an object of file to maintain several functions of file such as creating, reading, writing and update also
--> deleting the file
#how to open a file
1.open(): this open function takes two parameters and in this we have to close the file by calling
close() fucntion after program....
#1.file name
#2.mode
_____2.with open()_______
Modes "r","w","a","x""t"
        1."r"-read
        to read the file we will this mode and if the file doesn't exist.it will through the error

#read mode("r"):
-->to read files we will use this mode and if the file doesn't exist, it will through the error 
any = open("text_python.txt","r")
print(any.read())
any.close'

#write mode("w")
#--> we will use this mode to write the text into the file, it will create the file if it doesn't exist
----> it will overwrite new text with old text in the file...
any = open("textfile.txt","w")
any.write("Hello Kavya Moyyi")
any.close()

#append mode("a")
-->to add the text the file this is used and it will create the file if it doesn't exist
any = open("textfile.txt","a")
any.write("   Excellent!")
any.close()

#create mode("x"):
---> this is used to create the file , but is the file already exists in the system it will rise an error.
any=open("textfile.txt","x")



#To raed lines
   1.raed()
   2.readline()
   3.readlines()
#read()
#--->this method read the file chunck by chunck and we can also specify the size
any = open("textfile.txt","w")
any.write("Hello!\nKavya Moyyi")
any.close()

any = open("textfile.txt","a")
any.write("   Excellent!")
any.write("   Awesome!")
any.write("   Gorgeous!")
any.close()

any=open("textfile.txt","r")
print(any.read())
any.close()


#readline():
#-->this method can only read one line at a time
any=open("textfile.txt","r")
print(any.read())
any.close()

#readlines():
#-->This method can read the entire file and return into list with each line
#       is once
any = open("textfile.txt","r")
print(any.readlines())
any.close()

any = open("textfile.txt","r")
print(any.readlines(1))#using index
any.close()'''

with open("textfile.txt","r") as any:
    print(any.read())
any.close()










