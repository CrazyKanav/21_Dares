import tkinter as tk
from tkinter import *
import socket
from _thread import *

name = input("Enter your name: ")

print("Waiting for people to join")

opp = ''

print(opp)


root = Tk()
root.title("21 Dares")
canvas = Canvas(width=800,height=350)
root.geometry("800x600")
para="Basically, a online multiplayer game where players will take turns saying numbers 1,2 or\n 	 3 and it will add up to the main thing, the person whose number reaches 21 has to do a dare.\n Dare will ask that person to turn on the webcam and the other players will ask that person to \ndo a dare. In 3 mins that person has to do the dare. "
label_head = tk.Label(root, text="Welcome To 21 Dares",font=('Arial,',40),foreground='gold3')
label_head.pack()
# Create the first label
label1 = tk.Label(root, text=name,font=('Arial',40)).place(x=380,y=420)

# Create the second label
label2 = tk.Label(root, text=opp,font=('Arial',40)).place(x=1040,y=420)

def start_game():
    root.destroy()
    root2 = Tk()
    root2.title("21 Dares")
    root2.geometry("1500x800")
    w= root2.winfo_screenwidth()               
    h= root2.winfo_screenheight()  
    canvs2 = tk.Canvas(root2, height=900, width=1500)
    turn_lb=tk.Label(root2,text="dash was here",font=('Arial', 40)).place(x=625,y=100)
    
    label = tk.Label(root2, text=0, bg='gray',font=('Arial', 40)).place(x=775,y=10)
    
    bt_1=tk.Button(root2,text="1",font=('Calibri',35),foreground='black',background="light goldenrod yellow",width=5)
    bt_1.place(x=420, y=280)
    bt_2=tk.Button(root2,text="2",font=('Calibri',35),foreground='black',background="light goldenrod yellow",width=5)
    bt_2.place(x=720, y=280)
    bt_3=tk.Button(root2,text="3",font=('Calibri',35),foreground='black',background="light goldenrod yellow",width=5)
    bt_3.place(x=1020, y=280)

    canvs2.pack()
    root2.mainloop()


label_desp = tk.Label(root,text=para,font=('Arial',20),foreground='green')
label_desp.pack(padx=5,pady=120)
start_button=tk.Button(root,text="Start the game",font=('Calibri',35),foreground='brown',command = start_game).place(x=600,y=600)

root.mainloop()