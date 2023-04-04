# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:08:18 2021

@author: 0526p
"""
from tkinter import *

root = Tk()
mylabel = Label(root, text = "I'm your assistant! May")
mylabel_2 = Label(root, text = "What can I do for you?").grid(row = 2, column = 1)
mylabel_3 = Label(root, text = "  ").grid(row = 1)

mylabel.grid(row = 0, column = 0)
mylabel_2
mylabel_3
root.mainloop()
