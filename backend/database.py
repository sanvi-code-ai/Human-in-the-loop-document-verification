from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:sanvi@localhost:5432/hitl_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()