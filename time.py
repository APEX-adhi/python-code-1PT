from calendar import SATURDAY
from tkinter import *
import tkinter
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clocks")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Roboto-Thin", 80), background="black", foreground="cyan")
label.pack(anchor="center")

time()

mainloop()
