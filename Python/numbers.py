#Use of some functions related to numbers
#from math import * #imports evrything from math and no namespace of functions inside module now alreaduy known to ineterpreter
#Above way of importing is not recommended
import math
import random
#1 -- Mathematical Functions
print(abs(-4))
print(math.ceil(2.5))
print(math.log10(5))
print(math.log(math.e))
print(math.sqrt(25))
print(round(3.5149,2))
#2 -- Trignometric Functions
print(math.asin(0)/math.pi*180)
print(math.acos(0)/math.pi*180)
print(math.sin(math.radians(30)))
print(math.tan(math.radians(30)))
print(math.atan2(3,4))
#Other functions are similar and nothing is hard
#3 -- Random Functions
names = ["Vishvajeet","Piyush","Anuraag","Apurva"]
print(random.choice(names))
random.seed(random.randrange(0,100000000000000000))
print(random.random())
print(random.shuffle(names))
print(names)