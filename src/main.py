import os
from docx import document
from src.ocr import process_image

# Define input image and output Word file
IMAGE_PATH = "data/sample.png" # imame file
OUTPUT_DOCX = "output;result.docx"

def save_to_word(text, output_file):
    '''Save extracted text into a Word document.'''
    doc = Document()
    doc.add_paragraph(text)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    doc.save(output_file)

def main():
    '''Main funcion to process an image and save extracted text ot Word.'''
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: image file '{IMAGE_PATH}' not foud.")
        return
    
    extracted_text = process_image(IMAGE_PATH)

    save_to_word(extracted_text, OUTPUT_DOCX)

    print("Text extracted and saved to: ", OUTPUT_DOCX)
    print("Extracted Text: \n", extracted_text)

if __name__ == "__main__":
    main()