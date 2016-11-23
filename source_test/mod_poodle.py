'''	
	POODLE DEMO --- Without Handshaking
	This Program illustrates working of POODLE attack but no handshaking is shown
	This program is written from windows point of view in Python 3.5
	Author: Vishvajeet Patil
'''
import crypto   #Same as Crypto package on linux systems. 
import sys
sys.modules['Crypto'] = crypto  #Makes crypto module workable on windows systems
from crypto import Random #Imports cryptographically Secure Random module
from crypto.Cipher import AES #Imports AES cipher
import hmac
import hashlib
#Key and IV(Initialization Vector) generation 

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

#Function to generate Random key and iv when required
def generate():
	global key
	key = Random.new().read(AES.block_size)
	global iv
	iv = Random.new().read(AES.block_size)
#Function to pad messages
def pad(s):
	'''This function returns the padded message for given parameter string s according to PKCS7 standard
		which is used with AES ciphers'''
	n = AES.block_size
	return s + ((n - len(s) % n) * bytes([(n - len(s) % n)]))

#Function to unpad messages
def unpad(s):
	'''This function returns the true and unpadded version of given parameter string s according to PKCS7 standard
		which is used with AES ciphers if the padding is correct otherwise it returns false and string as it is'''
	if (s[len(s)-1]>AES.block_size):
		return False,s
	for ch in s[-1*s[len(s)-1]:]:
		if ch!=s[len(s)-1]:
			return False,s
	return  True,s[:-s[len(s)-1]]  #This implies remove the last padding character as many times as it's value from given string to get the
									#unpadded string

def encrypt(message):
	'''This function returns the encrypted version of the passed message using AES-256 in CBC(Cipher Block Chaining Mode'''
	generate()
	data = bytes(message) #Encoding the message is must 
	#Now the hash of the message
	hash = hmac.new(key,data,hashlib.sha256).digest()
	raw = data + hash
	#Now encryption
	cipher = AES.new(key,AES.MODE_CBC,iv)
	enc_message = iv + cipher.encrypt(pad(raw))
	return enc_message

def decrypt(enc_message):
	'''This function returns the decrypted version of the passed message'''
	#Now Decryption of message
	iv = enc_message[:AES.block_size]
	cipher = AES.new(key,AES.MODE_CBC,iv)
	dec_ret = unpad(cipher.decrypt(enc_message[AES.block_size:])) #Decrypt the message by removing the IV which is of the size AES.block_size
																  #and then unpad it
	dec_message = dec_ret[1]
	pad_flag = dec_ret[0]
	nhash = hmac.new(key,dec_message[:-32],hashlib.sha256).digest()
	if nhash != dec_message[-32:]:
		#print("Verification Failed")
		return False,pad_flag,dec_message
	return True,pad_flag,dec_message
def helper(precipher,curcipher,ignlist):
	n = AES.block_size
	nblock = []
	for t in range(n-1,-1,-1):   #The bytes in opposite order
		flag = False
		for num in range(0,256,1):
			if (not((t,num) in ignlist)):
				precipher_copy = precipher.copy()
				for ti in range(t+1,n,1):
					precipher_copy[ti] = precipher_copy[ti]^(n-t-1)^(n-t)
				precipher_copy[t] = precipher_copy[t]^num^(n-t)
				precipher_copy.extend(curcipher)
				nstr = bytes(precipher_copy)
				if decrypt(nstr)[1]==True:
					#print(num)
					flag = True
					precipher = precipher_copy[:AES.block_size]
					nblock.append(num)
					break;
		if not flag:
			ignlist.add((t+1,nblock[len(nblock)-1]))
			return False,[]
	return True,nblock

def getbytestr(inp):
	'''This function returns the byte array for the given input string inp'''
	raw_str = list(map(ord,inp))
	return bytes(raw_str)

def poodle_test(inp):
	'''
		This function implements the test poodle attack on inp string which it itself encrypts using AES-CBC and returns
		a tuple (Boolean,Decrypted bytestring<contains HMAC and Padding>)
		Use unpad function to unpad the bytestring
		NOTE - Input is string denoting plaintext
	'''
	raw_str = list(map(ord,inp))
	oblocks = list(zip(*[iter(raw_str)]*AES.block_size))
	encr_str = encrypt(raw_str)
	#Note This file does not use handshake (when doing that we have to probably use two files and not just one to show actual POODLE Demo)
	b_plainlist = [] #plaintext in form of byte list
	plainblocks = []
	#Thw below list will contain all the blocks that we need
	blocks = list(zip(*[iter(encr_str)]*AES.block_size))
	for cibpos in range(0,len(blocks)-1):
		precipher = list(blocks[cibpos]) #This is the block whose bytes we are going to change to get the next block
		curcipher = list(blocks[cibpos+1]) #This is the block whose plaintext is we are obtaining
		ignlist = set([])
		helper_bool =  False
		while not helper_bool:
			helper_ret = helper(precipher,curcipher,ignlist)
			helper_bool = helper_ret[0]
			nblock = helper_ret[1]
		nblock.reverse()
		b_plainlist.extend(nblock)
		plainblocks.append(tuple(nblock))
	b_plaintext = bytes(b_plainlist)
	return plainblocks[:-3]==oblocks,b_plaintext

def poodle(inp):
	'''
		This function implements the actual poodle attack on inp bytestring which is already encrypted using AES-CBC and returns
		a bytestring which is a decrypted String<contains HMAC and Padding>
		Use unpad function to unpad the bytestring
		NOTE - Input is bytestring denoting encrypted secret
	'''
	encr_str = inp
	#Note This file does not use handshake (when doing that we have to probably use two files and not just one to show actual POODLE Demo)
	b_plainlist = [] #plaintext in form of byte list
	plainblocks = []
	#Thw below list will contain all the blocks that we need
	blocks = list(zip(*[iter(encr_str)]*AES.block_size))
	for cibpos in range(0,len(blocks)-1):
		precipher = list(blocks[cibpos]) #This is the block whose bytes we are going to change to get the next block
		curcipher = list(blocks[cibpos+1]) #This is the block whose plaintext is we are obtaining
		ignlist = set([])
		helper_bool =  False
		while not helper_bool:
			helper_ret = helper(precipher,curcipher,ignlist)
			helper_bool = helper_ret[0]
			nblock = helper_ret[1]
		nblock.reverse()
		b_plainlist.extend(nblock)
		plainblocks.append(tuple(nblock))
	b_plaintext = bytes(b_plainlist)
	return b_plaintext

class poodleerror(RuntimeError):
	def __init__(self,*arg):
		self.args = arg
