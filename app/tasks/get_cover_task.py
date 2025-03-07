from fastapi import BackgroundTasks
from app.services.fetch_cover_service import FetchCoverService


def fetch_cover(book_id: int):
    """Fetch the book cover from the Minio server"""
    url = FetchCoverService().fetch_cover(book_id)

    return url
