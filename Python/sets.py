#Sets in python.Order is not important

set1 = {"India","Nepal","USA","Japan","UK"}

#Operations on set
#printing a set
print(set1)
#Checking if value is in set or not
print("India" in set1)
print("Russia" in set1)
#Looping through a dictionary
for x in set1:
	print(x)
#Unpacking values
a,*b = set1
print(a)
print(b)