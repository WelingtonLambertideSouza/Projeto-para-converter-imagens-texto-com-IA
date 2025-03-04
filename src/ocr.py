import pytesseract
from PIL import Image

# Define the image path
image_path = "./data/sample.png"

# Use Tesseract with Brazilian Portugese (por)
text = pytesseract.image_to_string(Image.open(image_path), lang='por')

# Print the extracted text
print(text)