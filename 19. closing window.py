# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 03:01:51 2021

@author: 0526p
"""

from tkinter import *

root = Tk()

def on_closing():
    if messagebox.askokcancel('Quite', 'Do you want to quite?'):
        root.destroy()
    
root.protocol('WM_DELETEWINDOW', on_closing())
root.mainloop()