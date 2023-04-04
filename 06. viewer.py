# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:42:13 2021

@author: 0526p
"""
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Live Logging Face Recognition Attendance System')
root.iconbitmap('C:/Users/0526p/Pictures/implementation/LLFRAS.ico')

myImg_1 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/LLFRAS.ico'))
myImg_2 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/mask.png'))
myImg_3 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/download .tif'))
myImg_4 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/line.png'))
myImg_5 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/face detect.jpg'))
myImg_6 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/my resize image.png'))
myImg_7 = ImageTk.PhotoImage(Image.open('C:/Users/0526p/Pictures/implementation/red_color.jpg'))

myList = [myImg_1, myImg_2, myImg_3, myImg_4, myImg_5, myImg_6, myImg_7]

mylabel = Label(image = myImg_1)
mylabel.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global mylabel, back_button, forward_button
    
    mylabel.grid_forget()
    mylabel = Label(image = myList[image_number-1])
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))
    button_forward = Button(root, text = '>>', command = lambda: forward(image_number+1))
    
    if image_number == 7:
        button_forward = Button(root, text = '>>', state=DISABLED)    
    
    mylabel.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

def back(image_number):
    global mylabel, back_button, forward_button
    
    mylabel.grid_forget()
    mylabel = Label(image = myList[image_number-1])
    button_back = Button(root, text = '<<', command = lambda: back(image_number-1))
    button_forward = Button(root, text = '>>', command = lambda: forward(image_number+1))
    
    if image_number == 1:
        button_back = Button(root, text = '<<', state=DISABLED)    
    
    mylabel.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

button_back = Button(root, text = '<<', command = back)
button_exit = Button(root, text = 'Exit', command = root.destroy)
button_forward = Button(root, text = '>>', command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)

root.mainloop()
