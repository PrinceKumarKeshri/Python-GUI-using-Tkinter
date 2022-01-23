# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:33:19 2021

@author: 0526p
"""
from tkinter import *
root = Tk()
root.title('Main Window')
def launch():
    global second
    second = Toplevel()
    second.title('Child Window')
    Label(second, text = 'second window').pack()
    Button(second, text = 'show', command = lambda:[hide(), show()]).pack(pady = 10)
    
def show():
    root.deiconify()
    
def hide():
    second.withdraw()
    
Label(root, text = 'Main window').pack()
Button(root, text = 'Launch Window', command = lambda: [root.withdraw(), launch()]).pack(pady = 10)

root.mainloop()