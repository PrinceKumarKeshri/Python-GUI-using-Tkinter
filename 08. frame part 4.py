# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:27:56 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')

frame = LabelFrame(root, text = 'This is my Frame...', padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

Button(frame, text = "Don't Click Here!").grid(row = 0, column = 0)
Button(frame, text = "...or Here!").grid(row = 1, column = 1)

root.mainloop()
