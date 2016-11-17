'''	
	AES Encryption Demo
	This Program illustrates working of AES encryption . HMAC is also used.
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

#Function to pad messages
def pad(s):
	'''This function returns the padded message for given parameter string s according to PKCS7 standard
		which is used with AES ciphers'''
	n = AES.block_size
	return s + ((n - len(s) % n) * chr(n - len(s) % n)).encode('UTF-8')

#Function to unpad messages
def unpad(s):
	'''This function returns the unpadded version of given parameter string s according to PKCS7 standard
		which is used with AES ciphers'''
	return  s[:-ord(s[len(s)-1:])]  #This implies remove the last padding character as many times as it's value from given string to get the
									#unpadded string
message = "Attack at the night in the woods"
data = message.encode('UTF-8') #Encoding the message is must 
#Now the hash of the message
hash = hmac.new(key,data,hashlib.sha256).digest()
raw = data + hash
#Now encryption
cipher = AES.new(key,AES.MODE_CBC,iv)
enc_message = iv + cipher.encrypt(pad(raw))

#Now Decryption of message
cipher = AES.new(key,AES.MODE_CBC,iv)
dec_message = cipher.decrypt(enc_message[AES.block_size:]) #Decrypt the message by removing the IV which is of the size AES.block_size
print(unpad(dec_message)[:-32].decode('UTF-8')) #The output of decrypt function is unpadded aauming it is correct.The program demonstrating
												#the verification can be seen in aes-hmac-verify.py file.Then SHA256 hash is removed and
												#decoded using UTF-8

