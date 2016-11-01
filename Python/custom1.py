var1 = 3
class batman1:
	def __init__(self,x = 3):
		self.katrina = x
	def normal(self,x):
		print("%d"%(var1*x))
	def func(self):
		global var1
		var1 = 15
def printit():
	print(var1)