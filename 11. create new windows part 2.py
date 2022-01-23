# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 01:03:32 2021

@author: 0526p
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Working on Tkinter')

def open():
    
    # python treat local variable as garbage value and swap these values in the garbage collections
    # so we need to declare local variable as global variable
    global my_img
    top = Toplevel()
    top.title('Working on Tkinter')
    my_img = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation 2/bharti.png'))
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top, text = 'close window', command = top.destroy, fg = 'white', bg = 'navy').pack()

btn = Button(root, text = 'Open Second Window', command = open, fg = 'white', bg = 'navy').pack()

mainloop()