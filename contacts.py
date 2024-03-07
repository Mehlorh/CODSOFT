import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(contact)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()

def view_contact_list():
    if contacts:
        contact_list.delete(0, tk.END)
        for contact in contacts:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        messagebox.showinfo("Empty", "Contact list is empty, Please add a contact.")

def search_contact():
    search_term = search_entry.get()
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            found_contacts.append(contact)
    if found_contacts:
        search_result.delete(0, tk.END)
        for contact in found_contacts:
            search_result.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        messagebox.showinfo("Not Found", "No contacts found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("Contact Book")

    # Labels
    tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
    tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="e")
    tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e")
    tk.Label(root, text="Address:").grid(row=3, column=0, sticky="e")
    tk.Label(root, text="Search:").grid(row=5, column=0, sticky="e")

    # Entries
    global name_entry, phone_entry, email_entry, address_entry, search_entry
    name_entry = tk.Entry(root)
    phone_entry = tk.Entry(root)
    email_entry = tk.Entry(root)
    address_entry = tk.Entry(root)
    search_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)
    phone_entry.grid(row=1, column=1)
    email_entry.grid(row=2, column=1)
    address_entry.grid(row=3, column=1)
    search_entry.grid(row=5, column=1)

    # Buttons
    tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=5)
    tk.Button(root, text="View Contact List", command=view_contact_list).grid(row=6, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=2, pady=5)

    # Listbox
    global contact_list, search_result
    contact_list = tk.Listbox(root, width=40)
    contact_list.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
    search_result = tk.Listbox(root, width=40)
    search_result.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
