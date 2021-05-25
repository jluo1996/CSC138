# UDP client
from socket import*  #include Python's socket library

serverName = 'hostname' 
serverPort = 64101

clientSocket = socket(AF_INET, SOCK_DGRAM)  #SOCK_DGRAM indicates using UDP socket

message = raw_input('Input lowercase sentence:')    #get user keyboard input
clientSocket.sendto(message, ('', serverPort))  #Attach server name, port to message; send into socket

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    #client socket will receive from server with bufSize 2048
                                                                #received message stored in modifiedMessage     
                                                                #sender IP address and port number stored into serverAddress
                                                                
print modifiedMessage

clientSocket.close(); 