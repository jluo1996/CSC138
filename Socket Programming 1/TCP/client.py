from socket import*

serverName = 'servername'
serverPort = 40726

clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM indecates using TCP
clientSocket.connect(('', serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
