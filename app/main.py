from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
# from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor
import time

import models
from database import engine

from routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'postgres', cursor_factory=RealDictCursor) # cursor_factory - to get column names
        cursor = conn.cursor()
        print("Database conn was successful")
        break
    except Exception as error:
        print("Conn to DB failed")
        print("error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}