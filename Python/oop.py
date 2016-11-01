#Study of classes and objects
class impclass:
	"""This class is the test class."""
	xman = 0
	def __init__(self):
		print("I am constructor")
		self.xman = 5
	def iknowthis(self,idea):
		"""This is the method for changing the xman attribute"""
		self.xman = idea
	def __del__(self):
		print("The object with id %d is getting deleted"%(id(self)))

print("##############################################################################\n")
nwobject = impclass()
print(impclass.__doc__)
print(impclass.iknowthis.__doc__) #Prints the documentation string of 
print(type(impclass.__doc__))
nwobject.iknowthis(15)
print(nwobject.xman)
nwobject.timepass = True
print(hasattr(nwobject,'timepass'))
print(getattr(nwobject,'carmen','Null')) #carmen is not present as a attribute hence this will output the default value which is passed as third argument
print(nwobject.__dict__) #Prints the namespace of the object
delattr(nwobject,'timepass') #Deletes the timepass attribute
print(hasattr(nwobject,'timepass')) 

#Some built in attributes of classes
print("\n##############################################################################\n")
print(impclass.__dict__)
print(nwobject.__class__) #Prints the name of the class
print(nwobject.__module__) #The name of the module
print(impclass.__bases__)

#Garbage Collection Mechanism Display
print("\n##############################################################################\n")
nwobject = impclass()
print("The old object will be deleted before this point")

#Class inheritance 
print("\n##############################################################################\n")
class impsubclass(impclass):
	"""Example of single inheritance"""
	def __init__(self):
		print("Subclass is getting initialized")
		self.xman = 6

impulse = impsubclass()
print(impulse.xman) #Superclass or baseclass constructor is not called
print(impsubclass.__bases__) #Prints the baseclasses of the corresponding class in form of tuple

#Example pf Multiple inheritance
class special:
	def __init__(self):
		print("I am special")
	def __del__(self):
		print("I am special and me with id %d is getting deleted"%(id(self)))
	kat = 14
	def changer(self):
		self.kat = 17

class subclass(impclass,special): #Characteristics of first class have higher priority than the latter classes
	def outputit(self):
		print(self.xman,self.kat)

plasma = subclass()
plasma.outputit()
print(subclass.__bases__)
print(isinstance(plasma,subclass)) #As 'plasma' is instance of 'subclass' so answer will be true
print(isinstance(plasma,special)) #As 'plasma' is instance of 'subclass' whose one of the base class is 'special' this will be true
print(issubclass(subclass,impclass)) #As 'subclass' is subclass of 'impclass'
print(issubclass(subclass,impsubclass)) #This will be false as 'subclass' is not subclass of 'impsubclass'

print("\n##############################################################################\n")

#Overloading some important methods . Example of self has been explained before. Example of del has also been worked out
#So we will use the examples of cmp and repr and str
class derivedclass(impclass,special):
	__secretdata = 5
	def timer(self):
		print("The time is important concept in the world")
	def __lt__(self,x):
		return self.kat<x.kat
	def __eq__(self,x):
		return self.kat==x.kat
	def __str__(self):
		return "This is derivedclass object(%d %d)"%(self.xman,self.kat)

achondrite = derivedclass()
achondrite.changer()
skylake = derivedclass()
print(achondrite<skylake) #__cmp__ is no longer used for operator overloading.Now a days __lt__ and __eq__ is used.
print(str(skylake))

print("\n##############################################################################\n")
#Private variable access
#There are no private variables in this language and there is no way to avoid them from accessing it.