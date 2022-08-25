from fastapi import FastAPI, Form, File, UploadFile, Depends, status, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv, dotenv_values
import models
from models import gate
from config.db import engine, Session
from functions.jwt_encode_decode import decode

app = FastAPI(

    servers=[{
        "url": "http://127.0.0.1:8000",
        "description": "Local server"

    }]
)

models.gate.Base.metadata.create_all(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


secret_key = dotenv_values(dotenv_path='.env')['SECRET_KEY']
print(secret_key)

httpBasic = HTTPBearer(bearerFormat="JWT", scheme_name="Bearer")


@app.get("/")
async def root(token: str = Depends(httpBasic)):
    token.dict()
    bb = token.credentials
    b = await decode(bb)
    return {"message": b}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
