from model.user import User
from data import (conn, curs, get_db, IntegrityError)
from error import Missing, Duplicate

curs.execute("""create table if not exists 
                user(
                    name text primary key, 
                    hash text)""")
curs.execute("""create table if not exists 
                xuser(
                    name text primary key, 
                    hash text)""")

def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(name=name, hash=hash)

def model_to_dict(user: User) -> dict:
    return user.model_dump()

def get_one(name: str) -> User:
    qry = "select * from user where name=:name"
    params = {"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if not row:
        raise Missing(f"User {name} not found")
    return row_to_model(row)

def get_all() -> list[User]:
    qry = "select * from user"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(user: User, table: str = "user") -> User:
    qry = f"""insert into {table} values (:name, :hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError as e:
        raise Duplicate(f"User {user.name} already exists") from e
    return get_one(user.name)

def modify(name: str,user: User) -> User:
    qry = """UPDATE user
            SET name=:name,
                hash=:hash
            WHERE   name=:name_orig"""
    params = model_to_dict(user)
    params["name_orig"] = name
    curs.execute(qry, params)
    if curs.rowcount == 0:
        raise Missing(f"User {name} not found")
    return get_one(user.name)

def delete(name: str) -> bool:
    qry = "delete from user where name=:name"
    user = get_one(name)
    params = {"name":name}
    curs.execute(qry, params)
    if curs.rowcount == 0:
        raise Missing(f"User {name} not found")
    create(user, table="xuser")
    return True
