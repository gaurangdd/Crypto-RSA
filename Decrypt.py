from socket import * 
from Crypto.PublicKey import RSA 

serverPort = 12224 serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort)) 
serverSocket.listen(1) 
print ' The server is ready to receive \n'

connectionSocket, addr = serverSocket.accept() 
pvt_key = open('key.pem','rb').read() 
p = RSA.importKey(pvt_key) 
publickey = p.publickey() 
connectionSocket.send(publickey.exportKey()) 

data = connectionSocket.recv(8192) 
encrypted = eval(data) 
decrypted = p.decrypt(encrypted)

print '\n Decrypted text is : ' + decrypted 

connectionSocket.close()