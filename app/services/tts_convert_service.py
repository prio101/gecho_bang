import os
import requests
import logging
from fastapi import HTTPException
from app.minio import MinioUploader



class TtsConvertService:
    def __init__(self, texts: list, book_name: str):
        self.texts = texts.join(" ") # List of texts to convert to speech
        self.book_name = book_name
        self.text = None
        self.files_url = []

    def run(self) -> str:
        # Convert text to speech
        for i, text in enumerate(self.texts):
            body = {
                        "model": "kokoro",
                        "input": text,
                        "voice": "am_adam",
                        "response_format": "mp3",
                        "download_format": "mp3",
                        "speed": 1,
                        "stream": True,
                        "return_download_link": False,
                        "lang_code": "a", # a for american English
                        "normalization_options": {
                        "normalize": True,
                        "unit_normalization": False,
                        "url_normalization": True,
                        "email_normalization": True,
                        "optional_pluralization_normalization": True
                        }
                    }
            response = requests.post('http://localhost:8880/v1/audio/speech', json=body)

            if response.status_code != 200:
                logging.error(f"Error converting text to speech; please try again")
                return HTTPException(status_code=400, detail="Error converting text to speech; please try again")

            file_url = MinioUploader().upload_file(f"sounds/{self.book_name}/{self.book_name}-page-{i}.mp3", response.content)
            self.files_url.append(file_url)
        return self.files_url

