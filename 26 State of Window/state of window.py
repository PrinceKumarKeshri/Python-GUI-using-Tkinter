# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 00:45:59 2021

@author: 0526p
"""

from tkinter import *
root = Tk()

def ternary():
    global ternary_window
    ternary_window = Toplevel()
    
    def show_forward():
        Button(root, text = '>>', command= lambda:[root.withdraw(), secondary()]).grid(row = 2, column = 0)
        if 'withdrawn'==root.state():
            print(root.state())
            print('primary window is withdraw\n')
        elif 'normal' == root.state():
            print(root.state())
            print('primary window is deiconify\n')

    Label(ternary_window, text = 'You are on ternary window').grid(row = 0, column = 0)
    Button(ternary_window, text = '<<', command = lambda:[secondary_window.destroy(), ternary_window.destroy(), root.deiconify(), show_forward()]).grid(row = 1, column = 0)
    Button(ternary_window, text = 'Exit', command= lambda:[root.destroy()]).grid(row = 3, column = 0)

    
def secondary():
    global secondary_window
    secondary_window = Toplevel()
    
    def show_forward():
        Button(root, text = '>>', command= lambda:[root.withdraw(), secondary_window.deiconify()]).grid(row = 2, column = 0)
        if 'withdrawn' == secondary_window.state():
            print(secondary_window.state())
            print('secondary window is withdraw')
        else:
            print(secondary_window.state())
            print('Secondary window is not exists')
        if 'withdrawn'==root.state():
            print(root.state())
            print('primary window is withdraw\n')
        elif 'normal' == root.state():
            print(root.state())
            print('primary window is deiconify\n')

    Label(secondary_window, text = 'You are on secondary window').grid(row = 0, column = 0)
    Button(secondary_window, text = '<<', command = lambda:[secondary_window.withdraw(), root.deiconify(), show_forward()]).grid(row = 1, column = 0)
    Button(secondary_window, text = '>>', command= lambda:[secondary_window.withdraw(), root.withdraw(), ternary(), show_forward()]).grid(row = 3, column = 0)
    Button(secondary_window, text = 'Exit', command= lambda:[root.destroy()]).grid(row = 4, column = 0)
        
    
    
Label(root, text = 'You are on primary window').grid(row = 0, column = 0)
Button(root, text = 'Go', command= lambda:[root.withdraw(), secondary()]).grid(row = 1, column = 0)
Button(root, text = '>>', state =  DISABLED).grid(row = 2, column = 0)
Button(root, text = 'Exit', command= lambda:[root.destroy()]).grid(row = 3, column = 0)
root.mainloop()
