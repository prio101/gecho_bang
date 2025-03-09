"""Main API File"""
import logging
from app import FastAPI
from app import books_router
from app import users_router
from app import APP_TITLE, VERSION_NUMBER


app = FastAPI(title=APP_TITLE, version=VERSION_NUMBER)

# Logging
LOG = logging.getLogger(__name__)

# Include routers:
"""Router that is coming from api/routes/*.py"""
app.include_router(books_router)
app.include_router(users_router)
