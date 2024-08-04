import tkinter as tk
from tkinter import messagebox, simpledialog
contacts = {}
def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Input Error", "Name and phone number are required.")
def view_contacts():
    contact_list = "\n".join([f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}" for name, details in contacts.items()])
    if contact_list:
        messagebox.showinfo("Contacts", contact_list)
    else:
        messagebox.showinfo("Contacts", "No contacts found.")
def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    result = [f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}" for name, details in contacts.items() if query.lower() in name.lower() or query in details['phone']]
    if result:
        messagebox.showinfo("Search Results", "\n".join(result))
    else:
        messagebox.showinfo("Search Results", "No matching contact found.")
def update_contact():
    name = simpledialog.askstring("Update", "Enter name of contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Input", "Enter new phone number (leave blank if no change):")
        email = simpledialog.askstring("Input", "Enter new email (leave blank if no change):")
        address = simpledialog.askstring("Input", "Enter new address (leave blank if no change):")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Error", "Contact not found.")
def delete_contact():
    name = simpledialog.askstring("Delete", "Enter name of contact to delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Error", "Contact not found.")
def create_gui():
    root = tk.Tk()
    root.title("Contact Book")
    tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
    tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
    tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
    tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
    tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)
    root.mainloop()
if __name__ == "__main__":
    create_gui()
