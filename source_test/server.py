'''
	This File is written for testing of mod_poodle module.
	Author - Vishvajeet Patil
'''
import mod_poodle
import socketserver
import ssl
input_str = "Katrina"
print(mod_poodle.poodle_test(input_str)[1])
encr_str = mod_poodle.encrypt(list(map(ord,input_str)))
print(mod_poodle.poodle(encr_str))
###############################################################
#The Testing of secure server and client will be done below
###############################################################
class securessl(socketserver.BaseRequestHandler):
	def handle(self):
		self.request = ssl.wrap_socket(self.request,keyfile="privkey.pem",certfile="cert.pem",server_side=True,ssl_version=ssl.PROTOCOL_SSLv3,cert_reqs=ssl.CERT_NONE,ca_certs="cacert.pem",ciphers="AES128")
		print(self.request.compression())
		try:
			#data = self.request.recv(1048576)
			data = self.request.read()
			while data:
				print(mod_poodle.getbytestr("Message Received: ")+data)
				self.request.write(mod_poodle.getbytestr("You said..")+data)
				#data = self.request.recv(1048576)
				data = self.request.read()
		except ssl.SSLError as e:
			print(e)
		return
ssl_serverloc = ("127.0.0.1",6000)
ssl_server = socketserver.TCPServer(ssl_serverloc,securessl)
ssl_server.serve_forever()