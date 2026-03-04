from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    POSTGRES_USER: str = Field(..., env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(..., env='POSTGRES_PASSWORD')
    POSTGRES_DB: str = Field(..., env='POSTGRES_DB')
    POSTGRES_HOST: str = Field(..., env='POSTGRES_HOST')
    POSTGRES_PORT: int = Field(5432, env='POSTGRES_PORT')
    DATABASE_URL: str = Field('', env='DATABASE_URL')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    ALGORITHM: str = Field('HS256', env='ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env='ACCESS_TOKEN_EXPIRE_MINUTES')

    class Config:
        env_file = '.env'

settings = Settings()
