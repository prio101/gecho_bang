from pydantic import BaseSettings

class Settings(BaseSettings):
    """Settings for the application"""
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
      """Load environment variables from .env file"""
      env_file = '.env'

settings = Settings()
