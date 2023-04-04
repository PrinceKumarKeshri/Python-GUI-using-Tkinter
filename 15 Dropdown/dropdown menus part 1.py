# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:30:14 2021

@author: 0526p
"""

from tkinter import *

root = Tk()
root.title('Working on Tkinter')

clicked = StringVar()

drop = OptionMenu(root, clicked, 'Sunday',
                  'Monday',
                  'Tuesday',
                  'Wednesday',
                  'Thursday',
                  'Friday',
                  'Saturday')
drop.pack()

root.mainloop()
