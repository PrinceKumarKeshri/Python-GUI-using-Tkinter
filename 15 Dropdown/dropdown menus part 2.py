# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:30:14 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Working on Tkinter')

def show():
    myLabel = Label(root, text = clicked.get()).pack()

options = ['Sunday',
           'Monday',
           'Tuesday',
           'Wednesday',
           'Thursday',
           'Friday',
           'Saturday']

clicked = StringVar()

# it set the default values of option menu else it show nothing
clicked.set(options[0])

# if we do not use * in the presedence of list variable then it treat all the items of list as a common variable
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text = 'Show Selection', command = show).pack()

root.mainloop()
