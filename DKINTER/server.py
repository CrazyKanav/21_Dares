import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '10.0.65.5'
port = 12345
s.bind((host, port))

# Listen for incoming connections
s.listen(1)

while True:
    # Wait for a client to connect
    client, address = s.accept()
    print(f'Connection from {address} has been established.')

    # Start the game
    score = 0
    dares = ["Sing a song", "Do 10 push-ups", "Eat a spoonful of hot sauce", "Call your crush", "Wear a silly hat for the rest of the day"]
    for dare in dares:
        client.send(dare.encode())
        response = client.recv(1024).decode()
        if response == "completed":
            score += 1
        else:
            score -= 1
    client.send(f'Your final score is {score}'.encode())
    client.close()
