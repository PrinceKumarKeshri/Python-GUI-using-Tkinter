# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:07:31 2021

@author: 0526p
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Working on Tkinter')

r = IntVar()
r.set('1')

def clicked(value):
    mylabel = Label(root, text = value)
    mylabel.pack()
    
Radiobutton(root, text = 'Option 1', variable = r, value = 1, command = lambda: clicked(r.get())).pack()
Radiobutton(root, text = 'Option 2', variable = r, value = 2, command = lambda: clicked(r.get())).pack()


myButton= Button(root, text = 'Click Me!', command = lambda: clicked(r.get()))
myButton.pack()

mylabel = Label(root, text = r.get())
mylabel.pack()

mainloop()