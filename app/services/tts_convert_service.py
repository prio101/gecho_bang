import os
import requests
import logging
from fastapi import HTTPException
from app.minio import MinioUploader



class TtsConvertService:
    def __init__(self, text: str):
        self.text = text

    def convert(self) -> str:
        # Convert text to speech
        response = requests.post("https://api.stt.com/tts", json={"text": self.text})

        if response.status_code != 200:
            logging.error(f"Error converting text to speech; please try again")
            return HTTPException(status_code=400, detail="Error converting text to speech; please try again")

        file_name = f"{self.text[:10]}.mp3"
        file_url = MinioUploader().upload_file(file_name, response.content)

        return file_url

