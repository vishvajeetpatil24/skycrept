
# Table of girls ages with person ages with whom they are allowded to date with

def limit_age(x):
	x = x/2
	x += 7
	return x
for x in range(15,66):
	print(x,limit_age(x))
