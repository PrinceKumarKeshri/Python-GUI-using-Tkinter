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
#c.execute("""CREATE TABLE addresses(
 #       first_name text,
  #      last_name text,
   #     roll_no integer,
    #    phone_no interger,
     #   email_id text
      #  )""")

# Create Submit Function For database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :r_no, :p_no, :e_id)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'r_no': r_no.get(),
                  'p_no': p_no.get(),
                  'e_id': e_id.get(),
                })
    
    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    r_no.delete(0, END)
    p_no.delete(0, END)
    e_id.delete(0, END)
     
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    
    # Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + '\n'
    
    query_label = Label(root, text = print_records, anchor = W)
    query_label.grid(row = 8, column = 0, columnspan = 2, sticky = W+E)
    
    # Commit changes
    conn.commit()
    
    # Close connection
    conn.close()
    
    
    
# Create text Boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 1, column = 1, padx = 20)
l_name = Entry(root, width = 30)
l_name.grid(row = 2, column = 1, padx = 20)
r_no = Entry(root, width = 30)
r_no.grid(row = 3, column = 1, padx = 20)
p_no = Entry(root, width = 30)
p_no.grid(row = 4, column = 1, padx = 20)
e_id = Entry(root, width = 30)
e_id.grid(row = 5, column = 1, padx = 20)

# Create Text Box Labels
f_name_label = Label(root, text = 'First Name', anchor = W)
f_name_label.grid(row = 1, column = 0, sticky = W+E)
l_name_label = Label(root, text = 'Last Name', anchor = W)
l_name_label.grid(row = 2, column = 0, sticky = W+E)
r_no_label = Label(root, text = 'Roll No', anchor = W)
r_no_label.grid(row = 3, column = 0, sticky = W+E)
p_no_label = Label(root, text = 'Phone No', anchor = W)
p_no_label.grid(row = 4, column = 0, sticky = W+E)
e_id_label = Label(root, text = 'Email ID', anchor = W)
e_id_label.grid(row = 5, column = 0, sticky = W+E)

# Create Submit Button
submit_btn = Button(root, text = 'Save', command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
query_btn = Button(root, text = 'Get', command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()