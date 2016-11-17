#Xor Calculation rough work
import crypto   #Same as Crypto package on linux systems. 
import sys
sys.modules['Crypto'] = crypto  #Makes crypto module workable on windows systems
from crypto import Random #Imports cryptographically Secure Random module
from crypto.Cipher import AES #Imports AES cipher
m = 0^230^1^203
import hmac,hashlib
print(m)
def unpad(s):
	'''This function returns the true and unpadded version of given parameter string s according to PKCS7 standard
		which is used with AES ciphers if the padding is correct otherwise it returns false and string as it is'''
	for ch in s[-1*ord(s[len(s)-1:]):]:
		print(ch)
		if ch!=s[len(s)-1]:
			return False,s
	return  True,s[:-ord(s[len(s)-1:])]

def pad(s):
	'''This function returns the padded message for given parameter string s according to PKCS7 standard
		which is used with AES ciphers'''
	n = AES.block_size
	return s + ((n - len(s) % n) * bytes([(n - len(s) % n)]))
key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)
def encrypt(message):
	'''This function returns the encrypted version of the passed message using AES-256 in CBC(Cipher Block Chaining Mode'''
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
raw_str = list(map(ord,"Attack the royal practice ground in north quadrant.bbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
data = pad(bytes(raw_str))
print(encrypt(raw_str))
print(bytes([106]))
enc_list = list(zip(*[iter(encrypt(raw_str))]*AES.block_size))
print(enc_list)