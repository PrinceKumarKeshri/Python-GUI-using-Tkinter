# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 01:03:32 2021

@author: 0526p
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Working on Tkinter')

top = Toplevel()
top.title('Working on Tkinter')
my_img = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation 2/bharti.png'))
my_label = Label(top, image = my_img).pack()

mainloop()