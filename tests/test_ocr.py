import os
import pytesseract
from PIL import Image
import pytest

# Define the image path
IMAGE_PATH = "./data/sample.png"

def test_ocr_extraction():
    """Test if OCR correctly extracts text from an image."""

    if not os.path.exists(IMAGE_PATH):
        pytest.skip(f"Image file {IMAGE_PATH} not found, skipping test.")

    extracted_text = pytesseract.image_to_string(Image.open(IMAGE_PATH), lang='por')

    assert isinstance(extracted_text, str), "OCR output should be a string."
    assert len(extracted_text.strip()) > 0, "OCR should not return an empty string."
    assert any(char in extracted_text for char in "çáéíóúâêôãõ"), "OCR must detect Brazilian Portuguese special characters."

if __name__ == "__main__":
    pytest.main()