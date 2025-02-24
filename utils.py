import tkinter as tk

def add_placeholder(entry, placeholder):
    """Adds a placeholder to an entry field."""
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder))
    entry.bind("<FocusOut>", lambda event: restore_placeholder(event, placeholder))

def clear_placeholder(event, placeholder):
    """Clears placeholder when the user starts typing."""
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)

def restore_placeholder(event, placeholder):
    """Restores placeholder if the field is left empty."""
    if not event.widget.get():
        event.widget.insert(0, placeholder)
