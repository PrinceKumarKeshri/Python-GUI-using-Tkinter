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

def slide():
    my_label = Label(root, text = f'Horizontal= {horizontal.get()}').pack()
    my_label1 = Label(root, text = f'Vertical = {vertical.get()}').pack()
    root.geometry(str(horizontal.get())  + 'x' +str(vertical.get()))
    
my_btn = Button(root, text = 'Click Me!', command = slide).pack()
my_label = Label(root, text = f'Horizontal= {horizontal.get()}').pack()
my_label1 = Label(root, text = f'Vertical = {vertical.get()}').pack()

root.mainloop()
