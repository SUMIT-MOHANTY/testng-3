from sqlalchemy import create_engine
from backend.core.config import Settings
settings = Settings()
engine = create_engine(settings.sql_db_conn, echo=False, future=True)
