import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import tkinter as tk
from unittest.mock import patch, MagicMock
from Tkinter_OCR_Gui import select_file, copy_text, confirm_clear, clear_all


@pytest.fixture
def mock_tk():
    root = tk.Tk()
    text_box = tk.Text(root, height=10, width=50)
    text_box.pack()
    return root, text_box

@patch("tkinter.filedialog.askopenfilename", return_value="test.png")
@patch("pytesseract.image_to_string", return_value="Sample text")
@patch("PIL.Image.open")
def test_select_file(mock_open, mock_tesseract, mock_dialog, mock_tk):
    root, text_box = mock_tk
    select_file()
    assert text_box.get("1.0", tk.END).strip() == "Sample text"

@patch("tkinter.messagebox.showinfo")
def test_copy_text(mock_messagebox, mock_tk):
    root, text_box = mock_tk
    text_box.insert("1.0", "Copied text")
    copy_text()
    assert root.clipboard_get() == "Copied text"
    mock_messagebox.assert_called_once_with("Success", "Text copied to clipboard!")

@patch("tkinter.messagebox.askyesno", return_value=True)
def test_confirm_clear(mock_askyesno, mock_tk):
    root, text_box = mock_tk
    text_box.insert("1.0", "Some text")
    confirm_clear()
    assert text_box.get("1.0", tk.END).strip() == ""

def test_clear_all(mock_tk):
    root, text_box = mock_tk
    text_box.insert("1.0", "Some text")
    clear_all()
    assert text_box.get("1.0", tk.END).strip() == ""
