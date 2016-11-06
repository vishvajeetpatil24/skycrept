#Example of capturing specific exception
#Still room for improvement in this file
import os
import stat
try:
	fob = open("file.txt","r+")
except IOError:
	fob = open("file.txt","w+")
	fob.close()
	print("IOError has occured.Check for existency or permissions.")
else:
	fob.read()
	fob.close()
#Example of capturing multiple exceptions
try:
	foa = open("file.txt","r")
	foa.close()
	x = 3/0
except IOError:
	print("IOError has occured")
except ZeroDivisionError:
	print("Division By zero")
	os.remove("file.txt")
else:
	print("This should never run as 3/0 will raise exception")
#Example of assert statement .This statement is usec to check if input to the function is correct and output of the function is correct
#On error the AssertionError is raised
def func(x):
	try:
		assert (x>=0),"x should not be negative"
	except AssertionError:
		print("Check the assertion for \"func\" function")
		#sys.exit(1)   #This line is commented out to avoid program from closing
	return x*5
print(func(3))
print(func(-1))
#Example of try and finally block -- This was tougher to imitate but this is one possible way to write it
try:
	foa = open("file.txt","w+")
	try:
		foa.write("Hello world")
		foa.close()
		os.chmod("file.txt", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
		foa = open("file.txt","w")
	finally:
		foa.close()
		os.remove("file.txt")
except IOError:
	print("IOError has occurred")
try:
	os.remove("file.txt")
except:
	print("Error occurred while removing file.Change permission for file \"file.txt\" to 777 and delete it manually")

#Getting the cause of the error
try:
	x = 15/0
except ZeroDivisionError as Argument:
	print(Argument)

#Raising the exception
def check(x):
	if x>10:
		raise Exception(x)
	else:
		print("We are all good")
try:
	check(11)
except Exception as e:
	print("Error in check function as x is %d"%(e.args[0]))

#User Defined Exception
class neterror(RuntimeError):
	def __init__(self,arg):
		self.args = arg
try:
	raise neterror("Bad Domain Name")
except neterror as e:
	print(e.args)