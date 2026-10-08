from model.user import User
from error import Missing, Duplicate

fakes = [User(name="admin", hash="Bhasa@123"), User(name="user", hash="user@123")]

def find(name:str) -> User|None:
    for user in fakes:
        if user.name == name:
            return user
    raise None

def check_missing(name:str) -> None:
    if not find(name):
        raise Missing(f"User {name} not found")

def check_duplicate(name:str) -> None:
    if find(name):
        raise Duplicate(f"User {name} already exists")

def get_all() -> list[User]:
    return fakes

def get_one(name:str) -> User:
    check_missing(name)
    return find(name)

def create(user:User) -> User:
    check_duplicate(user.name)
    fakes.append(user)
    return user

def modify(name:str, user:User) -> User:
    check_missing(name)
    for i, u in enumerate(fakes):
        if u.name == name:
            fakes[i] = user
            return user

def delete(name:str) -> bool:
    check_missing(name)
    for i, u in enumerate(fakes):
        if u.name == name:
            del fakes[i]
            return True
    raise Missing(f"User {name} not found")
