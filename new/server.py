import socket
from _thread import *

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '10.0.65.5'
port = 12345
s.bind((host, port))

# Listen for incoming connections
s.listen(2)

def get_name():
    name_response = client.recv(2048).decode()
    return name_response

def threaded_clients(client):
    client.send(str.encode("In threaded client"))
    while True:
        data = client.recv(2048)
        response = 'Server message ' + data.decode('utf-8')
        if not data:
            break
        client.sendall(str.encode(response))
    client.close()


while True:
    # Wait for a client to connect
    client, address = s.accept()
    print(f'Connection from {address} has been established.')
    name = client.recv(1024).decode()
    print(name)

    start_new_thread(threaded_clients, (client, ))
    # Start the game
    # score = 0
    # dares = ["Sing a song", "Do 10 push-ups", "Eat a spoonful of hot sauce", "Call your crush", "Wear a silly hat for the rest of the day"]
    # for dare in dares:
    #     client.send(dare.encode())
    #     response = client.recv(1024).decode()
    #     if response == "completed":
    #         score += 1
    #     else:
    #         score -= 1
    # client.send(f'Your final score is {score}'.encode())
    # client.close()
