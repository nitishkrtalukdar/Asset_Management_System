import tkinter as tk
from gui import create_gui

# Create the main application window
root = tk.Tk()
root.title("Wealth Management Portfolio")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Initialize GUI components
create_gui(root)

# Start the Tkinter event loop
root.mainloop()
