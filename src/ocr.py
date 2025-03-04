import cv2
import pytesseract

def process_image(image_path):
    '''Extract text from an image using Tesseract OCR'''
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert to grayscale

    # Apply OCR
    text = pytesseract.image_to_string(gray)

    return text