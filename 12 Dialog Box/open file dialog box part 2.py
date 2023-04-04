# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 01:46:40 2021

@author: 0526p
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Working on Tkinter')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = 'C:/Users/0526p/Pictures/bharti', title = 'Select a File', filetypes = (('png files', '*.png'), ('all files', '*.*')))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image).pack()

my_btn = Button(root, text = 'Open File', command = open, fg = 'white', bg = 'navy').pack()

root.mainloop()
