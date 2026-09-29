from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
import fake.explorer as service
from typing import Optional
from error import Missing, Duplicate

router = APIRouter(prefix="/explorer")

@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name:str) -> Explorer | None:
    try:
        return service.get_one(name)
    except Missing as e:
        return HTTPException(status_code=404, detail=e.msg)

@router.post("", status_code=201)
@router.post("/",status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as e:
        return HTTPException(status_code=409, detail=e.msg)

@router.patch("/")
def modify(explorer:Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except Missing as e:
        return HTTPException(status_code=404, detail=e.msg)

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)

@router.delete("/{name}")
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as e:
        return HTTPException(status_code=404, detail=e.msg)
