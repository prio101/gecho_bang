import os
import pytesseract
import requests
from PIL import Image


class OcrExtractTextService:
    def __init__(self, image_path):
        self.image_path = image_path

    def extract_text(self):
        # OCR code here
        image = Image.open(self.image_path)
        text = pytesseract.image_to_string(image)
        os.remove(self.image_path)

        # create a text file
        text_file = self.image_path.replace(".jpg", ".txt")
        with open(text_file, 'w') as f:
            f.write(text)

