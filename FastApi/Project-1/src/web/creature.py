from fastapi import APIRouter, HTTPException
from src.model.creature import Creature
import src.data.creature as service
from typing import Optional

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    from service import creature as service
from error import Missing, Duplicate

router = APIRouter(prefix="/creature")

@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name:str) -> Creature | None:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.post("/")
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)

@router.patch("/")
def modify(creature:Creature) -> Creature:
    try:
        return service.modify(creature)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.put("/")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)

@router.delete("/{name}")
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)