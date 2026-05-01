# from fastapi import FastAPI, HTTPException, status , Path
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()

# users = {
#     1: {
#         "name":"Tom",
#         "website": "www.tom.com",
#         "age": 29,
#         "role": "developer"
#     },
#     2: {
#         "name":"Tom",
#         "website": "www.tom.com",
#         "age": 29,
#         "role": "developer"
#     }
# }

# @app.get("/")
# async def root():
#     return {"message": "Hello World hi"}

# # GET USERS
# @app.get("/users/{user_id}")
# def get_user(user_id: int = Path(...,description="The ID you want to get", gt=0)):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User not Found")
    
#     return users[user_id]

# class User(BaseModel):
#     name: str
#     website: str
#     age: int
#     role: str

# @app.post("/user")
# async def create_user(user: User):
#     new_id = len(users) + 1
    
#     users[new_id] = user.model_dump()
#     print(users)
#     return users[new_id]








from fastapi import FASTAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
