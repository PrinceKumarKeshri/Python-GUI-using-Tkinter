# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:27:56 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')

frame = LabelFrame(root, text = 'This is my Frame...', padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10)

Button(frame, text = "Don't Click Here!").pack()

root.mainloop()
