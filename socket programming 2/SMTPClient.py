from socket import*

msg = "I love computer networks!\r\n"
endmsg = "\r\n.\r\n"

sender = 'jianliangluo@csus.edu'        # sender's email address
receipient = 'jayluo1996@gmail.com'     # receipient's email address
subject = 'CSC139\r\n'  # subject of the email
fakeSender = 'jun.dai@csus.edu\r\n'     # fake sender address

# Choose a mail server (e.g. gaia.ecs.csus.edu ) and call it mailserver
mailserver = 'gaia.ecs.csus.edu';  # address for ECS mail server
serverPort = 25    #port number for ECS mail server

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM indicate TCP connection
clientSocket.connect((mailserver, serverPort))  # connect to ECS mail server

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'
    
# Send HELO command and print server response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'
    
# Send MAIL FROM command and print server response.
clientSocket.send('mail from: <' + sender + '>\r\n')
print clientSocket.recv(1024)

# Send RCPT TO command and print server response.
clientSocket.send('rcpt to: <' + receipient + '>\r\n')
print clientSocket.recv(1024)

# Send DATA command and print server response.
clientSocket.send('DATA\r\n')
print clientSocket.recv(1024)

# Send message data.
clientSocket.send('From: ' + fakeSender)
clientSocket.send('Subject: ' + subject)
clientSocket.send('To: ' + receipient + '\r\n')
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)       # end with single period
print clientSocket.recv(1024)

# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n')
print clientSocket.recv(1024)

clientSocket.close()