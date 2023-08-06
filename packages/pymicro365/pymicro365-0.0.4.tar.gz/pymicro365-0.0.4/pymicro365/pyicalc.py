import customtkinter as ct
import tkinter.messagebox
from customtkinter import *
from tkinter.constants import SUNKEN

window=ct.CTk()
window.title('Calculator')
window.winfo_width()
window.winfo_height()
frame=ct.CTkFrame(master=window, fg_color="skyblue")
window.resizable(False, False)
window.geometry("430x360")
frame.pack(padx=5, pady=5, fill='both', expand=True)
entry=ct.CTkEntry(master=frame,width=400, height=50, placeholder_text="Enter a number:", placeholder_text_color="orange", font=("Roboto", 20))
entry.grid(row=0,column=0,columnspan=3,ipady=2,pady=2)
entry.bind("<Return>", lambda event: equal())

def myclick(number):
    entry.insert(ct.END,number)

def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,ct.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")

def clear():
    entry.delete(0,ct.END)
    
button_1=ct.CTkButton(master=frame,text='1',command=lambda:myclick(1))
button_1.grid(row=1,column=0,pady=4)
button_2=CTkButton(master=frame,text='2',command=lambda:myclick(2))
button_2.grid(row=1,column=1,pady=4)
button_3=CTkButton(master=frame,text='3',command=lambda:myclick(3))
button_3.grid(row=1,column=2,pady=4)
button_4=CTkButton(master=frame,text='4',command=lambda:myclick(4))
button_4.grid(row=2,column=0,pady=4)
button_5=CTkButton(master=frame,text='5',command=lambda:myclick(5))
button_5.grid(row=2,column=1,pady=4)
button_6=CTkButton(master=frame,text='6',command=lambda:myclick(6))
button_6.grid(row=2,column=2,pady=4)
button_7=CTkButton(master=frame,text='7',command=lambda:myclick(7))
button_7.grid(row=3,column=0,pady=4)
button_8=CTkButton(master=frame,text='8',command=lambda:myclick(8))
button_8.grid(row=3,column=1,pady=4)
button_9=CTkButton(master=frame,text='9',command=lambda:myclick(9))
button_9.grid(row=3,column=2,pady=4)
button_0=CTkButton(master=frame,text='0',command=lambda:myclick(0))
button_0.grid(row=4,column=1,pady=4)

button_add=CTkButton(master=frame,text="+",command=lambda:myclick('+'))
button_add.grid(row=5,column=0,pady=2)

button_subtract=CTkButton(master=frame,text="-",command=lambda:myclick('-'))
button_subtract.grid(row=5,column=1,pady=2)

button_multiply=CTkButton(master=frame,text="*",command=lambda:myclick('*'))
button_multiply.grid(row=5,column=2,pady=2)

button_div=CTkButton(master=frame,text="/",command=lambda:myclick('/'))
button_div.grid(row=6,column=0,pady=2)

button_clear=CTkButton(master=frame,text="Clear",command=clear)
button_clear.grid(row=6,column=1,columnspan=2,pady=2)

button_equal=CTkButton(master=frame,text="=",command=equal)
button_equal.grid(row=7,column=0,columnspan=3,pady=2)

copyright = ct.CTkLabel(frame, text="© Copyright 2022-2023 Informatic365", bg_color="transparent", fg_color="transparent")
copyright.place(relx=0.005, rely=0.915)

window.bind("<Escape>", lambda event: exit())
window.mainloop()