from datetime import timedelta, datetime
import os
from jose import jwt
from model.user import User

if os.getenv("CRYPTID_JWT_SECRET"):
    from fake import user as data
else: 
    from data import user as data

from passlib.context import CryptContext

SECRET_KEY = "keep-it-secret-keep-it-safe"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def get_jwt_username(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise ValueError("Username not found in token")
        return username
    except jwt.JWTError as e:
        raise ValueError("Invalid token") from e

def get_current_user(token: str) -> User|None:
    if not (username := get_jwt_username(token)):
        return None
    if (user:= lookup_user(username)):
        return user
    return None

def lookup_user(username: str) -> User|None:
    if (user := data.get_one(username)):
        return user
    return None

def auth_user(username: str, password: str) -> User|None:
    if not (user := lookup_user(username)):
        return None
    if not verify_password(password, user.hash):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta|None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_all() -> list[User]:
    return data.get_all()

def get_one(name: str) -> User|None:
    return data.get_one(name)

def create(user: User) -> User:
    return data.create(user)

def modify(name: str, user: User) -> User:
    return data.modify(name, user)

def delete(name: str) -> bool:
    return data.delete(name)
