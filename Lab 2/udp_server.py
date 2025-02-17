from socket import * # Imports all socket-related symbols

serverPort = 12000 # Defines the port number the server will listen on

serverSocket = socket(AF_INET, SOCK_DGRAM) # Creates UDP socket (SOCK_DGRAM indicates UDP)

serverSocket.bind(('', serverPort)) # Binds the socket to all available interfaces on specified port

print("The server is ready to receive") # Indicates server is ready

while 1: # Infinite loop to handle multiple client requests
    message, clientAddress = serverSocket.recvfrom(2048) # Receives message and client address, buffer size 2048 bytes
    modifiedMessage = message.decode().upper() # Decodes received bytes and converts to uppercase
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # Sends encoded response back to client