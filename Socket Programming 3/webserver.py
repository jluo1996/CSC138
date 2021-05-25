from socket import *

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve..')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        
        if '/../' in filename:
            raise IOError
        while filename[0] == '/':
            filename = filename[1:]
            
        f = open(filename)
        outputdata = f.read()
        #connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n' + outputdata + '\r\n')
        #for i in range(0, len(outputdata)):
        #    connectionSocket.send(outputdata[i].encode())
        #connectionSocket.send('\r\n'.encode())

        print('Sucessful\n')
    
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())

        print('Not Sucessful\n')

    connectionSocket.close()


serverSocket.close()
