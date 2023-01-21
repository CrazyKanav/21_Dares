import tkinter as tk
from tkinter import *
root2 = Tk()
root2.title("21 Dares")
root2.geometry("1500x800")
w= root2.winfo_screenwidth()               
h= root2.winfo_screenheight()  
canvs2 = tk.Canvas(root2, height=900, width=1500)
count_bx = canvs2.create_rectangle(600,50,850,300,fill="DarkSeaGreen1")
ply1 = canvs2.create_oval(600,350,850,600,fill="lavender blush1")
ply2 = canvs2.create_oval(900,350,1150,600,fill="lavender blush1")
ply2 = canvs2.create_oval(300,350,550,600,fill="lavender blush1")
lb_count = canvs2.create_text(720,180,text="0",font=('Calibri',90))
bt_1=tk.Button(root2,text="1",font=('Calibri',25),foreground='black',background="light goldenrod yellow")
bt_1.place(x=420, y=700)
bt_2=tk.Button(root2,text="2",font=('Calibri',25),foreground='black',background="light goldenrod yellow")
bt_2.place(x=720, y=700)
bt_3=tk.Button(root2,text="3",font=('Calibri',25),foreground='black',background="light goldenrod yellow")
bt_3.place(x=1020, y=700)


canvs2.pack()
root2.mainloop()