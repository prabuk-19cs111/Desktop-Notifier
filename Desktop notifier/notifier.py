from tkinter import * 
from tkinter import messagebox


top = Tk()
top.iconbitmap('icon.ico')
top.title("EXAM reminder") 
  
top.geometry("200x100")

label = Label( top, text="Your Exam is in 10 minutes \n Get Ready !", relief=RAISED )
label.pack()

top.mainloop()  