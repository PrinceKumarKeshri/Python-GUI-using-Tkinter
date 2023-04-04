# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:00:44 2021

@author: 0526p
"""
from tkinter import *
root = Tk()

e = Entry(root, width = 50, fg = 'blue', bg = 'white', borderwidth = 10)
e.pack()
e.insert(0, 'Enter Text')

def myClick():
    mylabel = Label(root, text = 'Hey! I am your assistant May')
    mylabel.pack()

mybutton_1 = Button(root, text = 'Click me!', command = myClick, fg = 'blue', bg = 'yellow')
mybutton_1.pack()

def my_Click():
    hey = 'Hey! ' + e.get()
    mylabel = Label(root, text = hey)
    mylabel.pack()

mybutton_2 = Button(root, text = 'Tap it!', command = my_Click, fg = 'blue', bg = 'yellow')
mybutton_2.pack()



root.mainloop()
