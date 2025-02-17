from socket import * # Imports all symbols from the socket module

serverPort = 12000 # Defines the port number the server will listen on
serverSocket = socket(AF_INET,SOCK_STREAM) # Creates a TCP socket (SOCK_STREAM indicates TCP)
serverSocket.bind(('',serverPort)) # Binds the socket to local address and specified port
serverSocket.listen(1) # Sets up the socket to accept connections, with max queue of 1
print('The server is ready to receive') # Indicates server is ready

while 1: # Infinite loop to handle multiple clients sequentially
    connectionSocket, addr = serverSocket.accept() # Waits and accepts new connection, returns new socket and client address
    sentence = connectionSocket.recv(1024).decode() # Receives data from client and converts bytes to string
    capitalizedSentence = sentence.upper() # Converts received string to uppercase
    connectionSocket.send(capitalizedSentence.encode()) # Sends response converted to bytes
    connectionSocket.close() # Closes the connection with current client