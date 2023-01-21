import tkinter as tk
from tkinter import *

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
def start_game():
    count=0
    root.destroy()
    root2 = Tk()
    root2.title("21 Dares")
    root2.geometry("1500x800")
    w= root2.winfo_screenwidth()               
    h= root2.winfo_screenheight()  
    canvs2 = tk.Canvas(root2, height=900, width=1500)

    def update(count, final):
        final = int(count) + int(final)
        return final

    count_bx = canvs2.create_rectangle(600,50,850,300,fill="DarkSeaGreen1")
    ply1 = canvs2.create_oval(600,350,850,600,fill="lavender")
    ply1_lb = canvs2.create_text(725,475,text='2nd',font=('Calibri',90))
    ply2 = canvs2.create_oval(900,350,1150,600,fill="lavender")
    ply2_lb = canvs2.create_text(1025,475,text="3rd",font=('Calibri',90))    
    ply3 = canvs2.create_oval(300,350,550,600,fill="lavender")
    ply3_lb = canvs2.create_text(425,475,text="1st",font=('Calibri',90))
    var = 0
    lb_count = canvs2.create_text(720,180,text=var,font=('Calibri',90))
    global a
    a=0
    while count!=21: 
        def btn_fn():
            if a==1:
                if count+1<21:
                    count+1
                    var = count
                    lb_count = canvs2.create_text(720,180,text=var,font=('Calibri',90))
                elif count+1==21:
                    print("hello")
                else:
                    count=0
            elif a==2:
                if count+2<21:
                    count+2
                elif count+2==21:
                    print("hello")
                else:
                    count=0
            else:
                if count+3<21:
                    count+3
                elif count+3==21:
                    print("hello")
                else:
                    count=0
                


        
    def a1():
        a=1;
    def a2():
        a=2;
    def a3():
        a=3;

    bt_1=tk.Button(root2,text="1",font=('Calibri',25),foreground='black',background="light goldenrod yellow",command=lambda:[a1,btn_fn])
    bt_1.place(x=420, y=700)
    bt_2=tk.Button(root2,text="2",font=('Calibri',25),foreground='black',background="light goldenrod yellow",command=lambda:[a2,btn_fn])
    bt_2.place(x=720, y=700)
    bt_3=tk.Button(root2,text="3",font=('Calibri',25),foreground='black',background="light goldenrod yellow",command=lambda:[a3,btn_fn])
    bt_3.place(x=1020, y=700)

    canvs2.pack()
    root2.mainloop()


label_desp = tk.Label(root,text=para,font=('Arial',20),foreground='green')
label_desp.pack(padx=5,pady=120)
start_button=tk.Button(root,text="Start the game",font=('Calibri',35),foreground='brown',command = start_game)
start_button.pack(padx=5,pady=20)


root.mainloop()