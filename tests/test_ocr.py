# tests/test_ocr.py
import pytest
import os
from ocr import process_image

IMAGE_PATH = "data/sample.png" # Ensure this file exists for the test

def test_process_image() :
    """Test if the OCR funcion correctly extracts text from an image."""

    if not os.path.exists(IMAGE_PATH):
        pytest.skip(f"Image file {IMAGE_PATH} not found, skipping test.")

    extracted_text = process_image(IMAGE_PATH)

    # Check that the text is not empty
    assert extracted_text != "", "ocr extraction failed: Text is not empty"
    

    # Optionally, check that the text contains expected content or a keyword
    # For example, if you expect the word "sistemas" to be in the text:
    assert "sistemas" in extracted_text, "Expected text not found in OCR output"