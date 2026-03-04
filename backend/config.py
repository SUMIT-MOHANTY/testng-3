from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    sql_conn: str = Field(..., env="SQL_CONN")
    jwt_secret: str = Field("change_me", env="JWT_SECRET")
    jwt_algo: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
