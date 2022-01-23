# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:07:28 2021

@author: 0526p
"""

from tkinter import *

root = Tk()

def label():
    h = Scrollbar(frame_1, orient = 'horizontal')
    h.pack(side = BOTTOM, fill = X)
    v = Scrollbar(frame_1)
    v.pack(side = RIGHT, fill = Y)


    t = Text(frame_1, width = 25, height = 5, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
    
    label_list = [['Prince','Kumar'], ['Abhinandan','Kumar'], ['Vaishali', 'Yadav'], ['Prince','Kumar'],
                  ['Abhinandan','Kumar'], ['Vaishali','Yadav'], ['Prince','Kumar'], ['Abhinandan','Kumar'],
                  ['Vaishali','Yadav'], ['Prince','Kumar'], ['Abhinandan','Kumar'], ['Vaishali','Yadav']]

    for i in label_list:
        for j in i:
            t.insert(END, f'{j} ')
        t.insert(END,'\n')
    
    t.pack(side = TOP, fill = X)
    h.config(command = t.xview)
    v.config(command = t.yview)

global frame_1
frame_1 = LabelFrame(root, text = 'Scroll Frame', fg = 'white', bg = 'navy')
frame_1.grid(row = 0, column = 0)

label()

root.mainloop()