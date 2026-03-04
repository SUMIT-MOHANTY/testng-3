from pydantic import BaseSettings
class Settings(BaseSettings):
    AZURE_AD_TENANT_ID: str = "your-tenant-id"
    AZURE_AD_CLIENT_SECRET: str = "your-secret"
    JWT_SECRET_KEY: str = "change_me_to_a_strong_secret"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
settings = Settings()
