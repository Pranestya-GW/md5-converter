# interface.py

import tkinter as tk
from tkinter import messagebox
from modules.hash_calculator import calculate_md5
from modules.excel_exporter import save_to_excel

def process_input(text_area):
    """Process the input text and save results to an Excel file."""
    input_text = text_area.get("1.0", tk.END).strip()
    
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    
    lines = input_text.splitlines()
    results = [(line, calculate_md5(line)) for line in lines]
    
    # Save results to Excel
    save_to_excel(results)

def create_gui():
    """Create the main GUI window."""
    root = tk.Tk()
    root.title("MD5 Converter")

    text_area = tk.Text(root, height=20, width=50)
    text_area.pack(pady=10)

    convert_button = tk.Button(root, text="Convert to MD5 and Save to Excel",
                               command=lambda: process_input(text_area))
    convert_button.pack(pady=10)

    root.mainloop()
