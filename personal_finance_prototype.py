import tkinter as tk
from tkinter import ttk, messagebox
from alpha_vantage.timeseries import TimeSeries

# Alpha Vantage API Key
API_KEY = "YOUR_API_KEY"

# Fetch stock price
def fetch_price(asset_name, asset_type):
    if asset_type in ["stock", "forex"]:
        try:
            ts = TimeSeries(key=API_KEY)
            data, _ = ts.get_quote_endpoint(symbol=asset_name)
            return float(data["05. price"])
        except:
            return "Invalid"
    return None

# Create the main application window
root = tk.Tk()
root.title("Wealth Management Portfolio")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Store the portfolio data
portfolio = []

# Placeholder text functionality
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder))
    entry.bind("<FocusOut>", lambda event: restore_placeholder(event, placeholder))

def clear_placeholder(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)

def restore_placeholder(event, placeholder):
    if not event.widget.get():
        event.widget.insert(0, placeholder)

# Function to add an asset to the portfolio
def add_asset():
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

    # Add to portfolio
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

    # Reset input fields with placeholders
    asset_name_entry.delete(0, tk.END)
    add_placeholder(asset_name_entry, "Asset Name")
    
    quantity_entry.delete(0, tk.END)
    add_placeholder(quantity_entry, "Quantity")
    
    purchase_price_entry.delete(0, tk.END)
    add_placeholder(purchase_price_entry, "Purchase Price")
    
    purchase_date_entry.delete(0, tk.END)
    add_placeholder(purchase_date_entry, "Purchase Date")
    
    address_entry.delete(0, tk.END)
    address_entry.pack_forget()  # Hide address entry

# Function to handle asset type selection
def asset_type_changed(event):
    if asset_type_var.get() == "real estate":
        address_entry.pack(pady=5)
    else:
        address_entry.pack_forget()

# Function to sell an asset
def sell_asset(asset):
    sell_window = tk.Toplevel(root)
    sell_window.title("Sell Asset")
    sell_window.geometry("300x200")

    tk.Label(sell_window, text=f"Sell {asset['name']}", font=("Arial", 10)).pack(pady=10)
    
    quantity_label = tk.Label(sell_window, text="Quantity to sell:", font=("Arial", 10))
    quantity_label.pack(pady=5)
    
    quantity_entry = tk.Entry(sell_window, font=("Arial", 10))
    quantity_entry.pack(pady=5)

    def confirm_sell():
        sell_quantity = quantity_entry.get()
        if not sell_quantity.isdigit() or int(sell_quantity) > asset['quantity']:
            messagebox.showerror("Invalid Quantity", "Please enter a valid quantity to sell.")
            return
        
        asset['quantity'] -= int(sell_quantity)
        if asset['quantity'] == 0:
            portfolio.remove(asset)
        messagebox.showinfo("Asset Sold", f"{sell_quantity} of {asset['name']} sold.")
        sell_window.destroy()
    
    sell_button = tk.Button(sell_window, text="Sell", command=confirm_sell, font=("Arial", 10), bg="#f44336", fg="white")
    sell_button.pack(pady=10)

# Function to display portfolio in a table
def view_portfolio():
    portfolio_window = tk.Toplevel(root)
    portfolio_window.title("Portfolio")
    portfolio_window.configure(bg="#f0f0f0")

    asset_types = set(asset["type"] for asset in portfolio)

    for asset_type in asset_types:
        tk.Label(portfolio_window, text=f"{asset_type.capitalize()} Portfolio", font=("Arial", 12, "bold")).pack(pady=10)

        columns = ["Asset Name", "Quantity", "Purchase Price", "Purchase Date"]
        if asset_type == "real estate":
            columns.append("Address")

        tree = ttk.Treeview(portfolio_window, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)

        for asset in portfolio:
            if asset["type"] == asset_type:
                values = (asset["name"], asset["quantity"], asset["purchase_price"], asset["purchase_date"])
                if asset_type == "real estate":
                    values += (asset["address"],)
                tree.insert("", tk.END, values=values)

        tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Add Hold and Sell buttons
        for asset in portfolio:
            if asset["type"] == asset_type:
                hold_button = tk.Button(portfolio_window, text="Hold", command=lambda a=asset: messagebox.showinfo("Hold", f"Holding {a['name']}."), bg="#4CAF50", fg="white", font=("Arial", 10))
                hold_button.pack(pady=5)

                sell_button = tk.Button(portfolio_window, text="Sell", command=lambda a=asset: sell_asset(a), bg="#f44336", fg="white", font=("Arial", 10))
                sell_button.pack(pady=5)

# Create frames for better layout
frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
frame.pack(pady=20)

# Asset name entry
asset_name_entry = tk.Entry(frame, width=20, font=("Arial", 10))
add_placeholder(asset_name_entry, "Asset Name")
asset_name_entry.pack(pady=5)

# Asset type dropdown
asset_type_var = tk.StringVar()
asset_type_dropdown = ttk.Combobox(frame, textvariable=asset_type_var, state="readonly", font=("Arial", 10))
asset_type_dropdown['values'] = ["stock", "forex", "gold", "real estate", "mutual fund"]
asset_type_dropdown.set("Select Asset Type")
asset_type_dropdown.pack(pady=5)
asset_type_dropdown.bind("<<ComboboxSelected>>", asset_type_changed)  # Bind change event

# Quantity entry
quantity_entry = tk.Entry(frame, width=20, font=("Arial", 10))
add_placeholder(quantity_entry, "Quantity")
quantity_entry.pack(pady=5)

# Purchase price entry
purchase_price_entry = tk.Entry(frame, width=20, font=("Arial", 10))
add_placeholder(purchase_price_entry, "Purchase Price")
purchase_price_entry.pack(pady=5)

# Create a frame for purchase date and address to place them beside each other
date_address_frame = tk.Frame(frame, bg="#f0f0f0")
date_address_frame.pack(pady=5)

# Purchase date entry
purchase_date_entry = tk.Entry(date_address_frame, width=20, font=("Arial", 10))
add_placeholder(purchase_date_entry, "Purchase Date")
purchase_date_entry.pack(side=tk.LEFT, padx=5)

# Address entry (for real estate)
address_entry = tk.Entry(date_address_frame, width=20, font=("Arial", 10))
add_placeholder(address_entry, "Address (Real Estate Only)")
address_entry.pack_forget()  # Initially hide the address entry

# Frame for buttons
button_frame = tk.Frame(frame, bg="#f0f0f0")
button_frame.pack(pady=10)

# Add asset button
add_button = tk.Button(button_frame, text="Add Asset", command=add_asset, font=("Arial", 10), bg="#4CAF50", fg="white")
add_button.pack(side=tk.LEFT, padx=5)

# View portfolio button
view_button = tk.Button(button_frame, text="View Portfolio", command=view_portfolio, font=("Arial", 10), bg="#2196F3", fg="white")
view_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
