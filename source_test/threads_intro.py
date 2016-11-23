'''This is example code to show the threading behavior in python'''
import threading
import time
##################################################################

class nclass(threading.Thread):
	def __init__(self,name,delay,counter):
		threading.Thread.__init__(self)
		self.name = name
		self.counter = counter
		self.delay = delay
	def run(self):
		func(self.name,self.delay,self.counter)

def func(name,delay,counter):
	while counter>0:
		print(name+" "+str(counter)+" "+str(time.localtime()))
		time.sleep(delay)
		counter = counter - 1
	return

th1 = nclass("Thread-1",1,5)
th2 = nclass("Thread-2",2,5)

th1.start()
th2.start()
th1.join()
