import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    LEDGER_ENDPOINT: str = Field(default="https://mock-ledger.local", env="LEDGER_ENDPOINT")
    LEDGER_KEY: str = Field(default="your-ledger-key", env="LEDGER_KEY")
    DATABASE_URL: str = Field(default="postgresql+psycopg2://postgres:postgres@db:5432/postgres", env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
