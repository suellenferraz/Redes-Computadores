from socket import * # Imports all symbols from the socket module

serverName = 'localhost' # Defines the server address (same machine in this case)
serverPort = 12000 # Defines the port number to connect to

clientSocket = socket(AF_INET, SOCK_STREAM) # Creates TCP socket (SOCK_STREAM means TCP)
clientSocket.connect((serverName,serverPort)) # Establishes connection with server

sentence = input('Input lowercase sentence:') # Gets user input from keyboard
clientSocket.send(sentence.encode()) # Converts string to bytes and sends to server

modifiedSentence = clientSocket.recv(1024).decode() # Receives response and converts bytes to string
print('From Server:', modifiedSentence) # Prints the modified message from server

clientSocket.close() # Closes the connection
