from tkinter import * 
from tkinter import messagebox
from tkinter import StringVar
import scheduler
  
top = Tk()
top.iconbitmap('icon.ico')
top.title("EXAM reminder") 
  
top.geometry("500x200")  

hour = StringVar()  
minute = StringVar()
  
def fun():  
    messagebox.showinfo("Sheduler","You will be notified")
    strhour=hour.get()
    strminute=minute.get()
    ustime=strhour+":"+strminute
    scheduler.timeschedule(ustime) 

hourlabel = Label(top, text = "HOUR").place(x = 30,y = 50)

minutelabel = Label(top, text = "MINUTE").place(x = 30, y = 90)

e1 = Entry(top,textvariable=hour).place(x = 80, y = 50)

e2 = Entry(top,textvariable=minute).place(x = 80, y = 90) 

b1 = Button(text = "Schedule",command = fun,activeforeground = "red",activebackground = "pink")
  
b1.pack()  

   
  
top.mainloop()  