# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:34:51 2021

@author: 0526p
"""

from tkinter import *

branch_window = Tk()
def remove_branch():
    remove_branch_window = Toplevel()
    def deselect_button():
        for i in range(1, 6):
            check1 = Checkbutton(remove_branch_window, text = ' ')
            check1.grid(row=i, column=0)
            check1.deselect()
    
    for i in range(1, 6):
            check1 = Checkbutton(remove_branch_window, text = ' ')
            check1.grid(row=i, column=0)
            check1.deselect()
    
    Button(remove_branch_window, text = 'back', command = lambda: [deselect_button(),remove_branch_window.destroy(),branch_window.deiconify()]).grid(row = 100, column =0)
    Button(remove_branch_window, text = 'Exit', command = lambda: [branch_window.destroy()]).grid(row = 100, column =1)

Button(branch_window, text = 'deselect', command = lambda: [branch_window.withdraw(), remove_branch()]).grid(row = 0, column =0)
branch_window.mainloop()
    