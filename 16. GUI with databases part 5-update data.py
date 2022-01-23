# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:00:15 2021

@author: 0526p
"""

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

# Create a query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

    # Create cursor
    c = conn.cursor()

    # get into table
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    
    # Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[5]) + '\n'
    
    query_label = Label(root, text = print_records)
    query_label.grid(row = 11, column = 0, columnspan = 2)
    
    # Commit changes
    conn.commit()
    
    # Close connection
    conn.close()
    
# Create a function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

    # Create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM addresses")
    records = c.fetchall()
    #print(records)
    
    # Delete into table
    c.execute(f"DELETE from addresses WHERE oid = " + del_roll.get())
    del_roll.delete(0, END)

    # Commit changes
    conn.commit()
    
    # Close connection
    conn.close()
        
# Create edit function to update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

    # Create cursor
    c = conn.cursor()
    
    record_id = del_roll.get()
    
    c.execute("""UPDATE addresses SET
              first_name = :first,
              last_name = :last,
              roll_no = :roll,
              phone_no = :phone,
              email_id = :email
              
              WHERE oid = :oid""",
              
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'roll': r_no_editor.get(),
                  'phone': p_no_editor.get(),
                  'email': e_id_editor.get(),
                  'oid': record_id
                  })
    
    # Commit changes
    conn.commit()
    
    # Close connection
    conn.close()

    editor.destroy()

def edit():
    global editor
    editor = Toplevel()
    editor.title('Update a Record')
    # Create a database or connect to one
    conn = sqlite3.connect('C:/Users/0526p/.spyder-py3/GUI/address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = del_roll.get()
    # get into table
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    # Create global variables for text box names
    global f_name_editor, l_name_editor, r_no_editor, p_no_editor, e_id_editor
    
    # Create text Boxes
    f_name_editor = Entry(editor, width = 30)
    f_name_editor.grid(row = 1, column = 1, padx = 20)
    l_name_editor = Entry(editor, width = 30)
    l_name_editor.grid(row = 2, column = 1, padx = 20)
    r_no_editor = Entry(editor, width = 30)
    r_no_editor.grid(row = 3, column = 1, padx = 20)
    p_no_editor = Entry(editor, width = 30)
    p_no_editor.grid(row = 4, column = 1, padx = 20)
    e_id_editor = Entry(editor, width = 30)
    e_id_editor.grid(row = 5, column = 1, padx = 20)
    
    # Create Text Box Labels
    f_name_label = Label(editor, text = 'First Name', anchor = W)
    f_name_label.grid(row = 1, column = 0, sticky = W+E)
    l_name_label = Label(editor, text = 'Last Name', anchor = W)
    l_name_label.grid(row = 2, column = 0, sticky = W+E)
    r_no_label = Label(editor, text = 'Roll No', anchor = W)
    r_no_label.grid(row = 3, column = 0, sticky = W+E)
    p_no_label = Label(editor, text = 'Phone No', anchor = W)
    p_no_label.grid(row = 4, column = 0, sticky = W+E)
    e_id_label = Label(editor, text = 'Email ID', anchor = W)
    e_id_label.grid(row = 5, column = 0, sticky = W+E)
    
    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        r_no_editor.insert(0, record[2])
        p_no_editor.insert(0, record[3])
        e_id_editor.insert(0, record[4])
    
    # create a save button to save a record
    edit_btn = Button(editor, text = 'Save', command = update)
    edit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

    
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
del_roll = Entry(root, width = 30)
del_roll.grid(row   = 8, column = 1, padx = 20)

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
del_roll_label = Label(root, text = 'Select Roll', anchor = W)
del_roll_label.grid(row = 8, column = 0, sticky = W+E)

# Create Submit Button
submit_btn = Button(root, text = 'Save', command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
query_btn = Button(root, text = 'Get', command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
delete_btn = Button(root, text = 'Delete', command = delete)
delete_btn.grid(row = 9, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 94)
edit_btn = Button(root, text = 'Edit', command = edit)
edit_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop() 