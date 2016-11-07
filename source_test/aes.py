'''	
	AES Encryption Demo
	This Program illustrates working of AES encryption but no HMAC is shown.Check aes-hmac.py for that
	This program is written from windows point of view in Python 3.5
	Author: Vishvajeet Patil
'''
import crypto   #Same as Crypto package on linux systems. 
import sys
sys.modules['Crypto'] = crypto  #Makes crypto module workable on windows systems
from crypto import Random #Imports cryptographically Secure Random module
from crypto.Cipher import AES #Imports AES cipher
#Key and IV(Initialization Vector) generation 

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

#Now we create AES cipher object with above generated keys,iv and mode CBC which is vulnerable to POODLE attack
cipher = AES.new(key,AES.MODE_CBC,iv)

message = "Attack the ship with torpedo from submarine XYZ positioned at 3.12" #Sample cool sounding plaintext message

#Function to pad messages
def pad(s):
	'''This function returns the padded message for given parameter string s according to PKCS7 standard
		which is used with AES ciphers'''
	n = AES.block_size
	return s + (n - len(s) % n) * chr(n - len(s) % n)
enc_message = iv + cipher.encrypt(pad(message)) #The encrypted message

#Function to unpad messages
def unpad(s):
	'''This function returns the unpadded version of given parameter string s according to PKCS7 standard
		which is used with AES ciphers'''
	return  s[:-ord(s[len(s)-1:])]  #This implies remove the last padding character as many times as it's value from given string to get the
									#unpadded string
#Now for decryption we need to create the object of class AES again so that we can decrypt data
cipher = AES.new(key,AES.MODE_CBC,iv)
dec_message = cipher.decrypt(enc_message[AES.block_size:])
print(unpad(dec_message).decode('UTF-8')) #To convert byte string into character string in UTF-8 encoding