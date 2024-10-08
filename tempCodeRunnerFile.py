from tkinter import *
from tkinter import messagebox
import re

# Initialize window
root = Tk()
root.geometry('600x500')
root.config(bg='#d3f3f5')
root.title('Contact Management System')
root.resizable(0, 0)

contacts = []

# Validation function for numeric input
def validate_numeric_input(char):
    return char.isdigit() or char == ""

# Function to add contact
def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone_number and email and address:
        if validate_phone_number(phone_number):
            contacts.append([name, phone_number, email, address])
            update_contact_list()
            reset_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Phone number must be exactly 10 digits.")
    else:
        messagebox.showerror("Error", "All fields are required.")

# Function to validate phone number
def validate_phone_number(phone_number):
    return re.fullmatch(r'\d{10}', phone_number) is not None

# Function to update contact list
def update_contact_list():
    contact_listbox.delete(0, END)
    for contact in contacts:
        contact_listbox.insert(END, "{} - {}".format(contact[0], contact[1]))

# Function to search contact
def search_contact():
    search_term = search_entry.get()
    results = [c for c in contacts if search_term in c[0] or search_term in c[1]]
    contact_listbox.delete(0, END)
    for contact in results:
        contact_listbox.insert(END, "{} - {}".format(contact[0], contact[1]))
    if not results:
        messagebox.showerror("Search Result", "No contact found.")

# Function to view selected contact details
def view_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        name_entry.delete(0, END)
        name_entry.insert(0, contact[0])
        phone_entry.delete(0, END)
        phone_entry.insert(0, contact[1])
        email_entry.delete(0, END)
        email_entry.insert(0, contact[2])
        address_entry.delete(0, END)
        address_entry.insert(0, contact[3])
    else:
        messagebox.showerror("Error", "Please select a contact to view.")

# Function to update contact details
def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        name = name_entry.get()
        phone_number = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name and phone_number and email and address:
            if validate_phone_number(phone_number):
                contacts[index] = [name, phone_number, email, address]
                update_contact_list()
                reset_entries()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Phone number must be exactly 10 digits.")
        else:
            messagebox.showerror("Error", "All fields are required.")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")

# Function to delete contact
def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        result = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
        if result:
            del contacts[index]
            update_contact_list()
            reset_entries()
            messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

# Function to reset entry fields
def reset_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# Create GUI components
Label(root, text='Name:', font=("Times new roman", 14), bg='#d3f3f5').place(x=20, y=20)
name_entry = Entry(root, width=40)
name_entry.place(x=100, y=20)

Label(root, text='Phone Number (10 digits):', font=("Times new roman", 14), bg='#d3f3f5').place(x=20, y=60)
phone_entry = Entry(root, width=40, validate="key", validatecommand=(root.register(validate_numeric_input), '%S'))
phone_entry.place(x=200, y=60)

Label(root, text='Email:', font=("Times new roman", 14), bg='#d3f3f5').place(x=20, y=100)
email_entry = Entry(root, width=40)
email_entry.place(x=100, y=100)

Label(root, text='Address:', font=("Times new roman", 14), bg='#d3f3f5').place(x=20, y=140)
address_entry = Entry(root, width=40)
address_entry.place(x=100, y=140)

Button(root, text='Add Contact', font='Helvetica 12 bold', bg='#e8c1c7', command=add_contact).place(x=20, y=200)
Button(root, text='Update Contact', font='Helvetica 12 bold', bg='#e8c1c7', command=update_contact).place(x=150, y=200)
Button(root, text='Delete Contact', font='Helvetica 12 bold', bg='#e8c1c7', command=delete_contact).place(x=280, y=200)
Button(root, text='View Contact', font='Helvetica 12 bold', bg='#e8c1c7', command=view_contact).place(x=410, y=200)
Button(root, text='Search', font='Helvetica 12 bold', bg='#e8c1c7', command=search_contact).place(x=20, y=240)
Button(root, text='Reset', font='Helvetica 12 bold', bg='#e8c1c7', command=reset_entries).place(x=100, y=240)

contact_listbox = Listbox(root, width=80, height=15, bg="#f0fffc", font=('Times new roman', 12), borderwidth=3, relief="groove")
contact_listbox.place(x=20, y=280)

search_entry = Entry(root, width=30)
search_entry.place(x=100, y=250)

root.mainloop()
