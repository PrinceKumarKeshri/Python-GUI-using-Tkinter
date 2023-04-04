# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:27:56 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')

frame = LabelFrame(root, text = 'This is my Frame...', padx = 5, pady = 5)
frame.pack(padx = 100, pady = 100)

Button(frame, text = "Don't Click Here!").pack()

root.mainloop()
