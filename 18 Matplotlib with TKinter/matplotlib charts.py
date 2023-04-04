# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:07:16 2021

@author: 0526p
"""

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Working on Matplotlib with Tkinter')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    #plt.hist(house_prices, 50)
    #plt.hist(house_prices)
    #plt.hist(house_prices, 200)
    #plt.pie(house_prices)
    plt.polar(house_prices)
    plt.show()


my_button = Button(root, text = 'Graph It!', command = graph)
my_button.pack()

root.mainloop()
