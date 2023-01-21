import socket
import tkinter

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '10.0.65.5'
port = 12345
s.connect((host, port))

print('Connected to the server')

# Send name 



# Close the socket
s.close()
