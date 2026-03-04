from pydantic import BaseSettings

class Settings(BaseSettings):
    sql_connection_string: str = "sqlite:///./test.db"
    jwt_secret_key: str = "change_me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
