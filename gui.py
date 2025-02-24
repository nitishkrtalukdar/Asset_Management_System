import tkinter as tk
from tkinter import ttk, messagebox
from portfolio import add_asset, view_portfolio
from utils import add_placeholder

def create_gui(root):
    """Sets up the main GUI components."""
    
    # Create frames
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

    # Quantity entry
    quantity_entry = tk.Entry(frame, width=20, font=("Arial", 10))
    add_placeholder(quantity_entry, "Quantity")
    quantity_entry.pack(pady=5)

    # Purchase price entry
    purchase_price_entry = tk.Entry(frame, width=20, font=("Arial", 10))
    add_placeholder(purchase_price_entry, "Purchase Price")
    purchase_price_entry.pack(pady=5)

    # Purchase date entry
    purchase_date_entry = tk.Entry(frame, width=20, font=("Arial", 10))
    add_placeholder(purchase_date_entry, "Purchase Date")
    purchase_date_entry.pack(pady=5)

    # Address entry (for real estate)
    address_entry = tk.Entry(frame, width=20, font=("Arial", 10))
    add_placeholder(address_entry, "Address (Real Estate Only)")
    address_entry.pack_forget()

    def asset_type_changed(event):
        """Show/hide address entry for real estate."""
        if asset_type_var.get() == "real estate":
            address_entry.pack(pady=5)
        else:
            address_entry.pack_forget()

    asset_type_dropdown.bind("<<ComboboxSelected>>", asset_type_changed)

    # Buttons
    button_frame = tk.Frame(frame, bg="#f0f0f0")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Add Asset", command=lambda: add_asset(
        asset_name_entry, asset_type_var, quantity_entry, purchase_price_entry, purchase_date_entry, address_entry
    ), font=("Arial", 10), bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)

    tk.Button(button_frame, text="View Portfolio", command=view_portfolio, font=("Arial", 10), bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)

