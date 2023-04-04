# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 05:13:43 2021

@author: 0526p
"""

from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text = 'Choosen a number').grid(row =1, column = 0)
number_choosen = ttk.Combobox(root, width = 20)
number_choosen['values'] = (2021, 2022, 2023, 2024, 2025, 2026, 2027,  2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2050)
number_choosen.grid(row = 2, column = 0)
number_choosen.current(0)
root.mainloop()
