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
#    response = messagebox.showinfo('This is my Popup!', 'Hello World!')
 #   response = messagebox.showwarning('This is my Popup!', 'Hello World!')
  #  response = messagebox.showerror('This is my Popup!', 'Hello World!')
    
    response = messagebox.askquestion('This is my Popup!', 'Hello World!')
    if response == 'yes':
        Label(root, text = 'You Clicked Yes!').pack()
    else:
        Label(root, text = 'You Clicked No!!').pack()
    
#    response = messagebox.askokcancel('This is my Popup!', 'Hello World!')
 #   if response == 1:
  #      Label(root, text = 'You Clicked Ok!').pack()
   # else:
    #    Label(root, text = 'You Clicked Cancle!!').pack()
    
    
#    response = messagebox.askyesno('This is my Popup!', 'Hello World!')
 #   if response == 1:
  #      Label(root, text = 'You Clicked Yes!').pack()
   # else:
    #    Label(root, text = 'You Clicked No!!').pack()
    

Button(root, text = 'Popup', command = popup).pack()

mainloop()
