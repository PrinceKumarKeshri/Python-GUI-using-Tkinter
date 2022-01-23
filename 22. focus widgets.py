# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 02:07:17 2021

@author: 0526p
"""

from tkinter import *

root = Tk()

def focus(button):
    widget = root.focus_get()
    print(widget, 'has focused')
    

e1 = Entry(root)
e1.insert(0, 'Enter text')
e1.pack(expand = 1, fill = BOTH)

e2 = Button(root, text = 'Button')
e2.focus_set()
e2.pack(pady = 5)

e3 = Radiobutton(root, text = 'Hello')
e3.pack(pady = 5)

root.bind_all('<Button-1>', lambda e: focus(e))

root.mainloop()