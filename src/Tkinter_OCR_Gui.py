import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
from PIL import Image
import shutil
import os

# Function to check if Tesseract is installed
def check_tesseract():
    if not shutil.which("tesseract"):
        messagebox.showerror("Error", "Tesseract-OCR not found!\nPlease install it and configure the path.\nLink to download: https://github.com/tesseract-ocr/tesseract")
        return False
    return True

# Function to open file dialog and extract text
def select_file():
    if not check_tesseract():
        return # Stop execution if Tesseract is missing

    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if file_path:
        extracted_text = pytesseract.image_to_string(Image.open(file_path), lang='por')
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, extracted_text)

# Function to copy text to clipboard
def copy_text():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        messagebox.showinfo("Sucess", "Text copied to clipboard!")

# Function to confirm and clear all
def confirm_clear():
    if messagebox.askyesno("Confirmation", "You really want to clear the text?"):
        clear_all()

# Function to clear text and memory
def clear_all():
    text_box.delete("1.0", tk.END)
    root.clipboard_clear()

# Create GUI
root = tk.Tk()
root.title("OCR Text Extractor")
root.geometry("1000x800")

btn_select = tk.Button(root, text="Select PNG", command=select_file)
btn_select.pack(pady=10)

btn_copy = tk.Button(root, text="Copy Text", command=copy_text)
btn_copy.pack(pady=5)

btn_clear = tk.Button(root, text="Clear All", command=confirm_clear)
btn_clear.pack(pady=5)

text_box = tk.Text(root, height=40, width=120)
text_box.pack(pady=10)

root.mainloop()