from socket import * 
from Crypto.PublicKey import RSA

serverName = '127.0.0.1' 
serverPort = 12224 
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort))

server_string = clientSocket.recv(8192) 
file_to_encrypt = open('asn1.txt','rb').read()

server_string = server_string.replace("public_key=", '') 
server_string = server_string.replace("\r\n", '')

o = RSA.importKey(server_string) 

read = file_to_encrypt 

print 'Original file is : ' + read

encrypted = o.encrypt(read,64) 
print encrypted 
clientSocket.send(str(encrypted)) 

clientSocket.close()