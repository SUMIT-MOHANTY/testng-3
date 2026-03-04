from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLite needs special connect_args, PostgreSQL does not
if "sqlite" in settings.sql_connection_string:
    engine = create_engine(settings.sql_connection_string, connect_args={"check_same_thread": False})
else:
    engine = create_engine(settings.sql_connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
