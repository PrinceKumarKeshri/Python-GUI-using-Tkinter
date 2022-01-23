# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 02:00:54 2021

@author: 0526p
"""

from tkinter import *

root = Tk()

colors = ['Blue', 'Gold', 'Red']

def radCall():
    redSel = radVar.get()
    if redSel == 0:
        root.configure(background = colors[0])
    elif redSel == 1:
        root.configure(background = colors[1])
    elif redSel == 2:
        root.configure(background = colors[2])
        
radVar = IntVar()

radVar.set(99)

for i in range(3):
    curRad = Radiobutton(root, text = colors[i], variable = radVar, value = i, command = radCall)
    curRad.grid(column = i, row = 5)
    
root.mainloop()