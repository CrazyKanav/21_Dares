import tkinter as tk
from tkinter import *
import time 

root3 = Tk()
root3.title("21 Dares")
canvas3 = Canvas(root3, height=500, width=795)
canvas3.create_rectangle(10,10,790,430,outline ="black",fill ="white",width = 2)
canvas3.pack()
dare_txt_lb=tk.Label(root3,fg='black',text="What dare do you want to give?")


dare_txt=Entry(root3,fg='black',bg='palegreen1',font=('Arial',20)).place(x=50, y=230)
lb_done = tk.Label(root3,text="Did you do the dare?",font=('Arial',20),foreground='sea green')
lb_done.pack_forget()
bt_done = tk.Button(root3,text="Yes",font=('Calibri',25),foreground='black',background="lemon chiffon")
bt_done.pack_forget()

#Create Entry Widgets for HH MM SS
sec = StringVar()
Entry(root3, textvariable=sec, width = 2, font=('Arial',20)).place(x=220, y=120)
sec.set('00')
mins= StringVar()
Entry(root3, textvariable = mins, width =2, font=('Arial',20)).place(x=180, y=120)
mins.set('00')
hrs= StringVar()
Entry(root3, textvariable = hrs, width =2, font=('Arial',20)).place(x=142, y=120)
hrs.set('00')

#Define the function for the timer
def countdowntimer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)

      #Update the time
      root3.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
         lb_done.pack()
         bt_done.pack()
      times -= 1
      
Label(root3, font =('Arial',22), text = 'Set the Timer',foreground='chartreuse4').place(x=105,y=70)
Button(root3, text='START', bd ='2', bg = 'IndianRed1',font =('Arial',10), command = countdowntimer).place(x=167, y=165)

root3.mainloop()