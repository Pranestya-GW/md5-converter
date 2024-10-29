# MD5 Converter

This project provides a simple GUI application that takes text input, converts each line into an MD5 hash, and saves the results to an Excel file.

## Project Structure

- `main.py`: Main entry point for the application.
- `modules/`: Contains the `hash_calculator` and `excel_exporter` modules for MD5 hashing and Excel exporting, respectively.
- `gui/`: Contains the `interface` module for the Tkinter user interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pranestya-gw/md5-converter.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```bash
python main.py
```

This will open a GUI where you can enter text, calculate MD5 hashes, and save them to an Excel file.
