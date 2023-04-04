# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:05:46 2021

@author: 0526p
"""
from tkinter import *
root = Tk()
root.title('Main Window')
def launch():
    global second
    second = Toplevel()
    second.title('Child Window')
    
def show():
    second.deiconify()
    
def hide():
    second.withdraw()
    
Button(root, text = 'Launch Window', command = launch).pack(pady = 10)
Button(root, text = 'Show', command = show).pack(pady = 10)
Button(root, text = 'Hide', command = hide).pack(pady = 10)

root.mainloop()
