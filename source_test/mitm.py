import socket
import socketserver
import crypto
import sys
import select
import struct
sys.modules['Crypto'] = crypto  #Makes crypto module workable on windows systems
from crypto import Random #Imports cryptographically Secure Random module
from crypto.Cipher import AES #Imports AES cipher
def getbytestr(inp):
    '''This function returns the byte array for the given input string inp'''
    raw_str = list(map(ord,inp))
    return bytes(raw_str)
class mitmserver(socketserver.BaseRequestHandler):
    def handle(self):
        count = 0
        destination = socket.create_connection(("127.0.0.1",6000))
        sockets = [self.request,destination]
        while True:
            inp, out, exce = select.select(sockets,[],[])
            for s in inp:
                if s == self.request:
                    data = s.recv(1048576)
                    count +=1
                    #print(data)
                    print("Going Content")
                    print(str(len(data)))
                    print(data)
                    '''
                    content,ver,length = struct.unpack('>BHH',data[:5])
                    if content==23:
                        header = data[:10]
                        payload = data[10:]
                        dat = list(zip(*[iter(payload)]*len(payload)))
                        block = list(dat[0])
                        block[len(block)-1] = 1;
                        nstr = header+bytes(block)
                        print(nstr)
                        destination.send(nstr)
                    else:
                    '''
                        #print(str(length)+" "+str(len(data)))
                    destination.send(data)
                elif s == destination:
                    data = s.recv(1048576)
                    if data == "":
                        break
                    content,ver,length = struct.unpack('>BHH',data[:5])
                    #print(content)
                    self.request.send(data)
        return

ssl_serverloc = ("127.0.0.1",6001)
ssl_server = socketserver.TCPServer(ssl_serverloc,mitmserver)
ssl_server.serve_forever()