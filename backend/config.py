import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    LOG_ENDPOINT: str = os.getenv('LOG_ENDPOINT', 'https://mock-logging.local')

settings = Settings()
