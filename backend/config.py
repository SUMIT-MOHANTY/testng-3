from pydantic import BaseSettings

class Settings(BaseSettings):
    AZURE_SUBSCRIPTION_ID: str = "your-subscription-id"
    AZURE_AD_CLIENT_ID: str = "your-client-id"
    SQL_CONNECTION_STRING: str = "postgresql://user:password@db:5432/dbname"
    JWT_SECRET_KEY: str = "changeme"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
