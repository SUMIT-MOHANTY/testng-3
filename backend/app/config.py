from pydantic import BaseSettings

class Settings(BaseSettings):
    LOG_ENDPOINT: str = "https://mock-logging.local"

    class Config:
        env_file = ".env"

settings = Settings()
