from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    sql_db_conn: str = Field('postgresql://user:pass@localhost/db', env='SQL_DB_CONN')
    secret_key: str = Field('change-me-please', env='SECRET_KEY')
    class Config:
        env_file = '.env'
