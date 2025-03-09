import os
import pytesseract
import requests
from PIL import Image


class OcrExtractTextService:
    def __init__(self, images_folder_path):
        self.images_folder_path = images_folder_path
        self.journal = []

    def run(self):
        # OCR code here
        images_folder_path = self.images_folder_path

        for image in os.listdir(images_folder_path):
            image_path = os.path.join(images_folder_path, image)
            with Image.open(image_path) as img:
                try:
                    n_frames = img.n_frames
                except AttributeError:
                    n_frames = 1

                for i in range(n_frames):
                    if n_frames > 1:
                        img.seek(i)
                    text = pytesseract.image_to_string(img)
                    self.journal.append(text)
                    print(text)
        # create a text file
        # text_file = self.image_path.replace(".jpg", ".txt")
        # with open(text_file, 'w') as f:
        #     f.write(text)
        return self.journal
