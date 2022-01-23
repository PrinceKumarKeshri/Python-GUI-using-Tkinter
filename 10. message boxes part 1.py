# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 00:34:52 2021

@author: 0526p
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Working on Tkinter')

# showinfo, showwarning, showerror, askquestion, askokcancle, askyesno

def popup():
    response = messagebox.showinfo('This is my Popup!', 'Hello World!')
#    response = messagebox.showwarning('This is my Popup!', 'Hello World!')
 #   response = messagebox.showerror('This is my Popup!', 'Hello World!')
  #  response = messagebox.askquestion('This is my Popup!', 'Hello World!')
   # response = messagebox.askokcancel('This is my Popup!', 'Hello World!')
    #response = messagebox.askyesno('This is my Popup!', 'Hello World!')
    Label(root, text = response).pack()

Button(root, text = 'Popup', command = popup).pack()

mainloop()