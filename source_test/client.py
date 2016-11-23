###############################################################
#The Testing of secure server and client will be done below.
#Threads are written in program 
###############################################################
import ssl
import socket
import pprint
import threading
import time
###############################################################
#Important Function for string to bytestring conversion
def getbytestr(inp):
	'''This function returns the byte array for the given input string inp'''
	raw_str = list(map(ord,inp))
	return bytes(raw_str)
###############################################################
p_rootsock = socket.socket()
p_rootsock = socket.create_connection(("127.0.0.1",6001))
rootsock = ssl.wrap_socket(sock=p_rootsock,ca_certs="cacert.pem",cert_reqs=ssl.CERT_REQUIRED,ssl_version=ssl.PROTOCOL_SSLv3,ciphers="AES128")
#ssl_serverloc = ("127.0.0.1",6000)
#rootsock.send(getbytestr("Hello"))
print(repr(rootsock.getpeername()))
print(rootsock.cipher())
print(pprint.pformat(rootsock.getpeercert()))
class readt(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.sock = sock
	def run(self):
		while True:
			raw_str = input("Input the message: ")
			self.sock.write(getbytestr(raw_str))
			time.sleep(0.1)

class writet(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.sock = sock
	def run(self):
		data = self.sock.read()
		while data:
			print("Received Transmission: "+data.decode("UTF-8"))
			data = self.sock.read()
#Create more of a client like we do in C program of client and socket
th1 = readt(rootsock)
th2 = writet(rootsock)
th1.start()
th2.start()
th1.join()
th2.join()