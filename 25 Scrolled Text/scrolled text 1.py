# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:48:51 2021

@author: 0526p
"""

from tkinter import *
from tkinter import scrolledtext
root = Tk()

Label(root, text = 'Notepad', fg = 'white', bg = 'navy', anchor = W).grid(row = 0, column = 0, sticky = W+E)
scrolledtext.ScrolledText(root, width = 30, height = 5, wrap = WORD).grid(row = 1, column = 0)
root.mainloop()
