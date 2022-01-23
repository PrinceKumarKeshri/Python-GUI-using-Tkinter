# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:33:26 2021

@author: 0526p
"""
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Live Logging Face Recognition Attendance System')
root.iconbitmap('C:/Users/0526p/Pictures/implementation/LLFRAS.ico')

myImg = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/LLFRAS.ico'))
mylabel = Label(image = myImg)
mylabel.pack()

button_quite = Button(root, text = 'Exit', command = root.destroy)
button_quite.pack()
root.mainloop()
