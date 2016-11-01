
#Dictionary in Python
dict = {1:"Katrina",2:"Emma",3:"Gemma",4:"Emily"}

#Operations on dictionary

#Printing whole dictionary directly
print(dict)
#printing a particular value using it's keys
print(dict[1])
#Loop through the dictionary - Way 1
for x in dict:
	print(x,dict[x])
#What is this function .items() ?
print(dict.items())
for (x,y) in dict.items(): #Using tuple
	print(x,y)
#####################################################
print(dict.items())
for x,y in dict.items(): #Using implied tuple
	print(x,y)
#Some functions related to the dictionary

#Length
print(len(dict))
#String representation
print(str(dict))
print(type(dict))
k = dict.copy()
print(k)
seq = [1,2,5,3]
dict1 = dict.fromkeys(seq)
print(dict1)
print(dict.values())
def cmp(x,y):
	return x>y
seq.sort()
print(seq)
print(cmp(2,2))