
#Playing with variable and function scope in python

#Before assignment of variable printing it. (Will not work as this is interpreted language)
'''
print(a)
a = 12
print(a)
'''
#After Function Declaration and use in function declaration but function is called later the variable assignment(Should work since m is just name of parameter 
#not argument and it is different from c because we have nothing like varibale declaration here)
def func():
	print(m)
m = 15
func()
#So in above case if variable assignment would have been above it would have still worked

#The below example does not work because it does not take variable from function scopes for another functions that might have got called in that scope
'''
def func2():
	print(l)
def func1():
	l = 15
	return func2()
func1()
'''
#Dynamic Scoping is not in this programming language
l = 10
def func2():
	print(l)
def func1():
	l = 25
	return func2()
func1()

#Use of global keyword.When variable is accessed inside a function for assignment then the variable is treated as local unless preceded
#by global <var> line
def func3():
	l = 19
	print(l)
func3()
def func4():
	#Assignment inside a function to a variable makes it treated as if being a local variable so the l on R.H.S is thought of as local variable
	#and since it does not have any value associated with it the below line will give a error
	#l = l +1
	print(l)	
func4()