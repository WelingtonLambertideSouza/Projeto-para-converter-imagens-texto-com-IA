import os 
import subprocess
from PIL import Image, ImageDraw, ImageFont

# Paths
PROJECT_PATH = r"C:\Users\Usuario\Documents\GitHub\Projeto-para-converter-imagens-texto-com-IA\tesseract_training"
IMAGE_FOLDER = os.path.join(PROJECT_PATH, "images")
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
FONT_PATH = os.path.join(PROJECT_PATH, "RedHatDisplay-VariableFont_wght.ttf") # Your custon font file
IMAGE_NAME = "custom_lang.tiff"
BOX_NAME = "custom_lang.box"
LANG_NAME = "custom_lang"

# Ensure output directories exist
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Funcion to creat an image with special characters
def generate_training_image(text="Á À Ã Â È É Ê Í Ì Î Õ Ô Ò Ó Ù Ú Û ã â á à è é í ì î õ ô ò ó ú ù û ç Ç"):
    img_size = (1100, 100) # Image size
    img = Image.new("RGB", img_size, color="white")
    draw = ImageDraw.Draw(img)

    # Load the font
    font = ImageFont.truetype(FONT_PATH, 40)

    # Draw the text
    draw.text((10, 10), text, font=font, fill="black")

    # Save TIFF image
    img_path = os.path.join(IMAGE_FOLDER, IMAGE_NAME)
    img.save(img_path)
    print(f"Training image saved: {img_path}")
    return img_path
    
# Generate box file using Tesseract
def generate_box_file():
    img_path = os.path.join(IMAGE_FOLDER, IMAGE_NAME)
    cmd = f'"{TESSERACT_PATH}" "{img_path}" "{IMAGE_FOLDER}\\{LANG_NAME}" batch.nochop makebox'
    print("Generating .box file...")
    subprocess.run(cmd, shell=True)
    print(f"box file generated: {IMAGE_FOLDER}\\{BOX_NAME}")

# Train Tesseract with the data
def train_tesseract():
    print("Starting Tesseract training process...")

    #Convert to .tr format
    subprocess.run(f'"{TESSERACT_PATH}" {IMAGE_FOLDER}\\{LANG_NAME}.tiff {IMAGE_FOLDER}\\{LANG_NAME} nobatch box.train', shell=True)

    # Computer character set
    subprocess.run(f'unicharset_extractor {IMAGE_FOLDER}\\{LANG_NAME}.box', shell=True)

    # Create font_proprieties file
    with open(os.path.join(IMAGE_FOLDER, "font_properties"), "w") as f:
        f.write("custom_font 0 0 0 0 0")

    # Train shape clustering
    subprocess.run(f'shapeclustering -F font_properties -U unichartset {IMAGE_FOLDER}\\{LANG_NAME}.tr', shell=True)

    # Train dictionary data
    subprocess.run(f'cntraining {IMAGE_FOLDER}\\{LANG_NAME}.tr', shell=True)

    print("Tesseract training completed.")

# Main function
if __name__ == "__main__":
    generate_training_image()
    generate_box_file()
    train_tesseract()