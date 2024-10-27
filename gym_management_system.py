import tkinter as tk
from tkinter import ttk

# Define the prices for each plan
plan_prices = {
    "Zumba": 500,
    "Cardio": 500,
    "Weightlifting": 1000,
    "All of Them": 1500,
}

# List to store member details
members = []

# Function to calculate the total price
def calculate_price():
    selected_plan = plan_var.get()
    price = plan_prices.get(selected_plan, 0)
    price_label.config(text=f"Total Price: ₹{price}pm")

# Function to add member details to the list and update the table
def add_member():
    name = name_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    plan = plan_var.get()
    price = plan_prices.get(plan, 0)

    members.append((name, phone, gender, plan, price))
    update_table()

    # Clear the input fields
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to update the table
def update_table():
    for i in tree.get_children():
        tree.delete(i)
    for member in members:
        tree.insert("", "end", values=member)

# Create the main window
root = tk.Tk()
root.title("Gym Management System")

# Create labels and entry fields for customer information
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar(value="Male")
gender_radiobutton1 = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_radiobutton2 = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_radiobutton1.pack()
gender_radiobutton2.pack()

# Create a dropdown menu for plan selection
plan_label = tk.Label(root, text="Select a Plan:")
plan_label.pack()
plan_var = tk.StringVar(value="Zumba")
plan_menu = tk.OptionMenu(root, plan_var, *plan_prices.keys())
plan_menu.pack()

# Button to calculate the price and add member
calculate_button = tk.Button(root, text="Calculate Price", command=calculate_price)
calculate_button.pack()

add_member_button = tk.Button(root, text="Add Member", command=add_member)
add_member_button.pack()

# Label to display the calculated price
price_label = tk.Label(root, text="Total Price: $0")
price_label.pack()

# Create a table to display member details
columns = ("Name", "Phone Number", "Gender", "Plan", "Price")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack()

# Start the GUI event loop
root.mainloop()
