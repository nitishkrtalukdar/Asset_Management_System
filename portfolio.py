import tkinter as tk
from tkinter import ttk, messagebox
from finance import fetch_price

# Store portfolio data
portfolio = []

def add_asset(asset_name_entry, asset_type_var, quantity_entry, purchase_price_entry, purchase_date_entry, address_entry):
    """Adds an asset to the portfolio."""
    asset_name = asset_name_entry.get()
    asset_type = asset_type_var.get()
    quantity = quantity_entry.get()
    purchase_price = purchase_price_entry.get()
    purchase_date = purchase_date_entry.get()
    address = address_entry.get() if asset_type == "real estate" else ""

    if asset_name == "Asset Name" or not quantity.isdigit() or not purchase_price.replace('.', '', 1).isdigit() or purchase_date == "Purchase Date":
        messagebox.showerror("Invalid Input", "Please enter valid values.")
        return

    current_price = fetch_price(asset_name, asset_type)
    if current_price == "Invalid":
        messagebox.showerror("Invalid Asset", f"{asset_name} is not a valid {asset_type}.")
        return

    portfolio.append({
        "name": asset_name,
        "type": asset_type,
        "quantity": int(quantity),
        "purchase_price": float(purchase_price),
        "purchase_date": purchase_date,
        "address": address,
        "current_price": current_price
    })
    messagebox.showinfo("Asset Added", f"{asset_name} added to portfolio.")

def view_portfolio():
    """Displays the portfolio in a new window."""
    portfolio_window = tk.Toplevel()
    portfolio_window.title("Portfolio")
    portfolio_window.configure(bg="#f0f0f0")

    tree = ttk.Treeview(portfolio_window, columns=("Asset Name", "Quantity", "Purchase Price", "Purchase Date"), show="headings")
    for col in ["Asset Name", "Quantity", "Purchase Price", "Purchase Date"]:
        tree.heading(col, text=col)
    
    for asset in portfolio:
        tree.insert("", tk.END, values=(asset["name"], asset["quantity"], asset["purchase_price"], asset["purchase_date"]))

    tree.pack(fill=tk.BOTH, expand=True, pady=10)

def sell_asset(asset):
    """Handles selling assets."""
    if asset in portfolio:
        portfolio.remove(asset)
        messagebox.showinfo("Asset Sold", f"{asset['name']} sold.")
