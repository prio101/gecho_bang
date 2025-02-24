"""Base Imports"""
from fastapi import FastAPI
from app.api.routes.books import router as books_router

# Constants
APP_TITLE = "Gecho Bang API"
VERSION_NUMBER = "1.0"
