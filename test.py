import tkinter as tk
from tkinter import ttk

# Create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Create a window
window = tk.Tk()

# Create a Treeview widget
tree = ttk.Treeview(window)

# Define the columns of the table
tree["columns"] = ("value")
tree.column("value", width=100)
tree.heading("value", text="Value")

# Add the items to the table
for key, value in my_dict.items():
    tree.insert("", "end", text=key, values=value)

# Pack the Treeview widget
tree.pack()

# Start the main event loop
window.mainloop()