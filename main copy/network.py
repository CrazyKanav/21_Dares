import socket

def ask():
    name = input("What is the player's name: ")
    print(f"Ok, {name}. \n WELCOME TO 21 DARES")
    return name


class Player:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.65.5"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def getName(self):
        return self.id

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048*2).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048*2).decode()
        except socket.error as e:
            print(e)
        
player = Player()
name = player.send(ask())
