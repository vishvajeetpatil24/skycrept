#This file will discuss about the File I/O in python programming language
import os
print("##############################################################################\n")
#Normal Print function
#Print single line
print("I love her")
print()
#Print Multiple lines
print("I asked her to be my gf","Her reply was be my best friend")

#Reading input from the screen
#Note - Python2 used to have function named raw_input which is now stands discontinued
str = input("Do you love me?If yes type y if no type n ")
print("And the response is "+str)

#Opening the files
file = open("..\\test.txt","r+")
print(type(file))
#Some attributes associated with file object
print(file.closed)
print(file.mode)
print(file.name)
#softspace sttribute is not supported in python 3
print("##############################################################################\n")
str = file.read()
print(str)
print(type(file.tell()))
print(file.tell())
file.seek(7,0)
print(file.read())
file.close()
#Directory Operations and functions related to that
if (os.path.isfile("test.txt")):
	os.rename("test.txt","..\\moved.txt")
else:
	newf = open("test.txt","w+")
	newf.write("I love India.India is my country.")
	newf.close()
	str = input("Do you want to move the test.txt? ")
	if (str.lower()=="y" or str.lower()=="yes"):
		os.rename("test.txt","..\\moved.txt")
if (not(os.path.isdir(".\\dirname"))):
	os.mkdir("dirname")
str = input("Do you want to delete newly created directory? ")
if (str.lower()=="y" or str.lower()=="yes"):
	os.rmdir("dirname")

#For reference view the tutorialspoint pages or python documentation