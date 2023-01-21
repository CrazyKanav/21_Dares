import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '10.0.65.5'
port = 12345
s.connect((host, port))

print('Connected to the server')

# Play the game
while True:
    dare = s.recv(1024).decode()
    if dare == "Your final score is":
        break
    print(f'Dare: {dare}')
    response = input("Enter 'completed' if you completed the dare, otherwise enter 'failed': ")
    s.sendall(response.encode())

# Print final score
final_score = s.recv(1024).decode()
print(final_score)

# Close the socket
s.close()
