from datetime import datetime, timedelta

from dotenv import dotenv_values
from jose import jwt

secret_key = dotenv_values(dotenv_path='.env')['SECRET_KEY']
algorithm = 'HS256'
expire_time = dotenv_values(dotenv_path='.env')['ACCESS_TOKEN_EXPIRE_MINUTES']


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def encode(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


async def decode(token: str):
    decoded_jwt = jwt.decode(token, secret_key, algorithms=algorithm)
    b=decoded_jwt.get('sub')
    return decoded_jwt