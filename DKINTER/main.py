import tkinter as tk
from tkinter import *
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '10.0.65.5'
port = 12345
s.connect((host, port))

print('Connected to the server')

root = Tk()
root.title("21 Dares")
canvas = Canvas(width=800,height=250)
root.geometry("800x600")
para="Basically, a online multiplayer game where players will take turns saying numbers 1,2 or\n 	 3 and it will add up to the main thing, the person whose number reaches 21 has to do a dare.\n Dare will ask that person to turn on the webcam and the other players will ask that person to \ndo a dare. In 3 mins that person has to do the dare. "
label_head = tk.Label(root, text="Welcome To 21 Dares",font=('Arial,',40),foreground='gold3')
label_head.pack()
canvas.create_rectangle(140,70,310,240,outline ="black",fill ="white",width = 2)
canvas.create_rectangle(330,70,500,240,outline ="black",fill ="white",width = 2)
canvas.create_rectangle(520,70,690,240,outline ="black",fill ="white",width = 2)
canvas.pack()
label_desp = tk.Label(root,text=para,font=('Arial',20),foreground='dark olive green')
label_desp.pack(padx=5,pady=120)
start_button=tk.Button(root,text="Start the game",font=('Calibri',35),foreground='sandy brown')
start_button.pack(padx=5,pady=20)
root.mainloop()
