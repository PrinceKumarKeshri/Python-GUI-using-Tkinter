# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:29:58 2021

@author: 0526p
"""

from tkinter import *
import sqlite3

root = Tk()
root.title('Working on Tkinter')

# Databases

# Create a database or connect to one
conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        roll_no integer,
        phone_no interger,
        email_id text
        )""")

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()