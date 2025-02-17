from socket import * # Imports all socket-related symbols

serverName = 'localhost'  # Sets server address to local machine
serverPort = 12000 # Defines the destination port number

clientSocket = socket(AF_INET, SOCK_DGRAM) # Creates UDP socket (SOCK_DGRAM indicates UDP)
message = input('Input lowercase sentence:') # Gets user input from keyboard
clientSocket.sendto(message.encode(), (serverName, serverPort)) # Sends encoded message to server with destination address
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # Receives response and server address, buffer size 2048 bytes

print(modifiedMessage.decode()) # Prints decoded message from server
clientSocket.close() # Closes the UDP socket