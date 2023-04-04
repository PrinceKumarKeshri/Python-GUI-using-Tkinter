# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:15:52 2021

@author: 0526p
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Working on Tkinter')

Toppings = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
    ]

pizza = StringVar()
pizza.set('Pepperoni')

for text, topping in Toppings:
    Radiobutton(root, text = text, variable = pizza, value = topping).pack(anchor = W)
    
def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()
    

myButton = Button(root, text = 'Click Me!', command = lambda: clicked(pizza.get()))
myButton.pack()

#myLabel = Label(root, text = pizza.get())
#myLabel.pack()

mainloop()
