from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal() # responsible for talking to DB
    try:
        yield db
    finally:
        db.close()

## below is for using raw sql
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'postgres', cursor_factory=RealDictCursor) # cursor_factory - to get column names
#         cursor = conn.cursor()
#         print("Database conn was successful")
#         break
#     except Exception as error:
#         print("Conn to DB failed")
#         print("error: ", error)
#         time.sleep(2)