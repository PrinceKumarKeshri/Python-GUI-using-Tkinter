# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 02:18:20 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Working on Tkinter')
root.geometry('400x400')

vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

horizontal = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()

root.mainloop()
