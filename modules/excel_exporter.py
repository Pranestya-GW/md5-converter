# excel_exporter.py

import pandas as pd
from tkinter import filedialog, messagebox

def save_to_excel(data):
    """Save the given data to an Excel file."""
    df = pd.DataFrame(data, columns=["Original Text", "MD5 Hash"])
    
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel Files", "*.xlsx")],
                                             title="Save as")
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", "MD5 hashes have been saved to Excel file.")
