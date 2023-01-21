import socket
from _thread import *

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '10.0.65.5'
port = 12345
s.bind((host, port))
s.listen(1)

client, address = s.accept()
print(f'Connection from {address} has been established.')

message = client.recv(1024).decode("utf-8")
