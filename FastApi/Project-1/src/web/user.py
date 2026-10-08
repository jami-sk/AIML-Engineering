import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User
from datetime import timedelta

if os.getenv("CRYPTID_JWT_SECRET"):
    from fake import user as service
else:
    from service import user as service

from error import Missing, Duplicate

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/user", tags=["user"])
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")

def unauthed():
    raise HTTPException(
        status_code=401, 
        detail="Icorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
        )

@router.post("/token")
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.name}, 
        expires_delta=expires_delta
        )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    user = service.get_current_user(token)
    if not user:
        unauthed()
    return {"username": user.name}

@router.get("/")
def get_all()-> list[User]:
    return service.data.get_all()

@router.get("/{name}")
def get_one(name:str)-> User:
    try:
        return service.data.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.post("/", status_code=201)
def create(user:User)-> User:
    try:
        return service.data.create(user)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)

@router.patch("/")
def modify(name:str, user:User)-> User:
    try:
        return service.data.modify(name, user)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.delete("/{name}")
def delete(name:str)-> bool:
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
    