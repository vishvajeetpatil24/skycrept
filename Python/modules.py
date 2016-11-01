print("##############################################################################\n")
import sys
import os
print(sys.path) #The default path to find the modules
PATH = os.getenv("PATH")
PYTHONPATH = os.getenv("PYTHONPATH")
#print(path)  #Should not work as python is case-sensitive
print(PATH)
print(PYTHONPATH) #Another place where the module can be found
print("##############################################################################\n")
#Keywords defined by the module or by class
print(dir(os))
print(os.__name__)
class test:
	x = 5
	def func():
		print("Hello world")
print(dir(test))
print("##############################################################################\n")
#Describes the use of locals() and globals() function
del PATH
del PYTHONPATH
kat = 15
bat = 12
def funct(m,p):
	global bat
	bat = p
	kat = m
	print(locals())  #At which location we are calling the locals() or globals() function is important
	print(globals())
	return kat
funct(3,4)
print("##############################################################################\n")
#imp.reload() function will use the custom user written module to display the functionality
#this function reloads the module.Writing import twice
import custom
import imp
nwobject = custom.batman()
nwobject.normal(3)
nwobject.func()
nwobject.normal(3)
imp.reload(custom)
nwobject.normal(3)
#Use of from <module_name> import <specific_namespace>
from custom1 import batman1
nwobject1 = batman1(5)
print("##############################################################################\n")
#If you wanna study about how packages in python work kindly visit the link below
#https://www.tutorialspoint.com/python3/python_modules.htm
#and see the packages section there