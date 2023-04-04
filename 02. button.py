# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:11:00 2021   

@author: 0526p
"""
from tkinter import *
root = Tk()
mybutton_1 = Button(root, text = 'Click Me!', state = DISABLED)
mybutton_2 = Button(root, text = 'Click It!', padx = 50)
mybutton_3 = Button(root, text = 'Click It!', pady = 40)
mybutton_4 = Button(root, text = 'Click It!', padx = 50, pady = 30)
mybutton_1.pack()
mybutton_2.pack()
mybutton_3.pack()
mybutton_4.pack()

def myClick():
    mylabel = Label(root, text = 'Hey! I am your assistant May')
    mylabel.pack()

mybutton_5 = Button(root, text = 'Click me!', command = myClick, fg = 'blue', bg = 'yellow')
mybutton_5.pack()

mybutton_6 = Button(root, text = 'Tap it!', command = myClick(), fg = 'yellow', bg = 'green')
mybutton_6.pack()
root.mainloop()
