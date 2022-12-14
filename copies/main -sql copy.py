# from typing import Optional
# from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
# from pydantic import BaseModel, HttpUrl
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# import models
# from database import engine, get_db
# from sqlalchemy.orm import Session

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None

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


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, {"title": "favorite food", "content": "I like pizza", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     return {"status": "success"}

# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts = cursor.fetchall()
#     return {"data": posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     # post_dict = post.dict()
#     # post_dict['id'] = randrange(0, 1000000)
#     # my_posts.append(post_dict)
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     # above are all staged changes, but not committed yet
#     conn.commit()
#     return {"data": new_post}

# @app.get("/posts/{id}") # path param is  string by default. need to convert manually
# def get_post(id:int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
#     post = cursor.fetchone()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
#     deleted_post = cursor.fetchone()
#     conn.commit()

#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT) # expected to not send any data back for 204


# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()

#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     return {"data": updated_post}