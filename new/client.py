import socket
import tkinter as tk
from tkinter import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server
host = '10.0.65.5'
port = 5556
s.connect((host, port))

print('Connected to the server')
name = input("What's your name: ")
print(name)

s.sendall(str.encode(name))

flag = s.recv(1042).decode()

if flag:
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
        label2 = tk.Label(root, text="opp",font=('Arial',40)).place(x=1040,y=420)

        def start_game():
            root.destroy()
            root2 = Tk()
            root2.title("21 Dares")
            root2.geometry("1500x800")
            w= root2.winfo_screenwidth()               
            h= root2.winfo_screenheight()  
            canvs2 = tk.Canvas(root2, height=900, width=1500)
            count_bx = canvs2.create_rectangle(600,50,850,300,fill="DarkSeaGreen1")
            ply1 = canvs2.create_oval(600,350,850,600,fill="lavender")
            ply1_lb = canvs2.create_text(725,475,text='1st',font=('Calibri',90))
            ply2 = canvs2.create_oval(900,350,1150,600,fill="lavender")
            ply2_lb = canvs2.create_text(1025,475,text="2nd",font=('Calibri',90)) 

            global count
            count = int(s.recv(2048).decode())

            label = tk.Label(root2, text=f"Counter: {count}", bg='gray',font=('Arial', 40))
            label.pack()

            # give increment to client, if odd then client's turn, if even then main's turn
            while count < 21:
                increment = s.recv(2048).decode()
                print("Increment " + increment)
                print("Count " + str(count))
                incre_str = str(increment)
                print(incre_str)

                def disable(b1, b2, b3):
                    b1.config(state="disable")
                    b2.config(state="disable")
                    b3.config(state="disable")

                def add(i):
                    increment = increment
                    global count
                    while (count + i) < 21:
                        break
                    count += i
                    label.config(text=f"Counter: {str(count)}")
                    print("INCREMENT HELLO")
                    increment += 1
                    print(increment)

                    print(f"SOCKET SENDING INCREMENT HERE {increment}")
                    print(f"SOCKET SENDING COUNT HERE {count}")
                    x = str(increment)
                    y = str(count)
                    client.sendall(str.encode(x)) # Increment
                    client.sendall(str.encode(y))
                

                if int(increment) % 2 == 0:
                    print("Even, Main's Turn")
                    bt_1=tk.Button(root2,text="1",font=('Calibri',25),foreground='black',background="light goldenrod yellow")
                    bt_1.place(x=420, y=700)
                    bt_2=tk.Button(root2,text="2",font=('Calibri',25),foreground='black',background="light goldenrod yellow")
                    bt_2.place(x=720, y=700)
                    bt_3=tk.Button(root2,text="3",font=('Calibri',25),foreground='black',background="light goldenrod yellow")
                    bt_3.place(x=1020, y=700)

                    disable(bt_1, bt_2, bt_3)


                else:
                    print("Odd, Client Turn")
                    increment = int(client.recv(1024).decode())
                    count = int(client.recv(1024).decode())
                    print(f"Increment: {increment} and Count: {count}")
                    #  Enabled Buttons
                    bt_1=tk.Button(root2,text="1",font=('Calibri',25),foreground='black',background="light goldenrod yellow",command=lambda: add(1))
                    bt_1.place(x=420, y=700)
                    bt_2=tk.Button(root2,text="2",font=('Calibri',25),foreground='black',background="light goldenrod yellow",command=lambda: add(2))
                    bt_2.place(x=720, y=700)
                    bt_3=tk.Button(root2,text="3",font=('Calibri',25),foreground='black',background="light goldenrod yellow",command=lambda: add(3))
                    bt_3.place(x=1020, y=700)
                

                canvs2.pack()
                root2.mainloop()


        label_desp = tk.Label(root,text=para,font=('Arial',20),foreground='green')
        label_desp.pack(padx=5,pady=120)
        start_button=tk.Button(root,text="Start the game",font=('Calibri',35),foreground='brown',command = start_game).place(x=600,y=600)

        root.mainloop()
else:
    print("You lost")

# Close the socket
s.close()
