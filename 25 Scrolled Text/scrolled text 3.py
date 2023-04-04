# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:07:28 2021

@author: 0526p
"""

from tkinter import *

root = Tk()

def label():
    h = Scrollbar(frame_3, orient = 'horizontal')
    h.pack(side = BOTTOM, fill = X)
    v = Scrollbar(frame_3)
    v.pack(side = RIGHT, fill = Y)


    t1 = Text(frame_3, width = 25, height = 5, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
    
    t2 = Text(frame_3, width = 25, height = 5, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
    label_list = ['Prince Kumar', 'Abhinandan Kumar', 'Vaishali Yadav', 'Prince Kumar',
                  'Abhinandan Kumar', 'Vaishali Yadav', 'Prince Kumar', 'Abhinandan Kumar',
                  'Vaishali Yadav', 'Prince Kumar', 'Abhinandan Kumar', 'Vaishali Yadav']

    for i in label_list:
        spli = i.split(' ')
        t1.insert(END, f'{spli[0]}')
        t2.insert(END, f'{spli[1]}')
        t1.insert(END,'\n')
        t2.insert(END,'\n')
    
    t2.pack(side = RIGHT, fill = X)
    t1.pack(side = TOP, fill = Y)
    h.config(command = t1.xview)
    v.config(command = t1.yview)
    h.config(command = t2.xview)
    v.config(command = t2.yview)

global frame_1, frame_2, frame_3
frame_1 = LabelFrame(root, text = 'Scroll Frame', fg = 'white', bg = 'navy')
frame_1.grid(row = 0, column = 0)
frame_2 = LabelFrame(frame_1)
frame_2.grid(row = 0, column = 0, rowspan = 1)
frame_3 = LabelFrame(frame_1)
frame_3.grid(row = 1, column = 0)

Label(frame_2, text = 'First Name', fg = 'purple').grid(row = 0, column = 0)
#Label(frame_2, text = ' '*98).grid(row = 0, column = 1, sticky = E+W)
Label(frame_2, text = 'Last Name', fg = 'purple').grid(row = 0, column = 2)


label()

root.mainloop()
