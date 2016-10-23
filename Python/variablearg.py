import sys
#Is there a concept of pointer in python?   Answer - No || Another Question - Then what is this * we use in variable arguments
#Variable args
def func(*args):
	kat = ""
	for x in args:
		kat += (" "+x)
	print(kat[1:])
func("Batwoman","Movie","Was great")
#Pointer concpt check - No starred argument is totally different thing
*kat,c,d = 1,2,3
total = 0
for x in kat:
	total += x
print(total)
#Another example of starred assignment
*kat, = 1,2,3
total = 0
for x in kat:
	total += x
print(total)
#yet another example of starred assignment -- The below gode does not work because of two starred expressions in assignment
*kat,*bat = 1,2,3,4
print(kat)
print(bat)