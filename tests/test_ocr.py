import src.ocr as ocr

def test_ocr():
    '''Test OCR processing with a sample image.'''
    text = ocr.process_image("data/test_1.png")
    assert isinstance(text, str) #insure the output is a string