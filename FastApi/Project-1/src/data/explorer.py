from src.data import conn, curs
from src.model.explorer import Explorer
from typing import Optional
from error import Missing, Duplicate

curs.execute("""CREATE TABLE if not exists explorer(
             name text primary key,
             description text,
             country text)""")

def row_to_model(row: tuple) -> Explorer:
    name, description, country = row
    return Explorer(name=name, description=description, country=country)

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump() if explorer else None

def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Explorer with name '{name}' not found.")

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(explorer: Explorer) -> Explorer:
    qry = """insert into explorer values (:name, :description, :country)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except Exception as e:
        raise Duplicate(f"Explorer with name '{explorer.name}' already exists.")
    return get_one(explorer.name)

def modify(explorer: Explorer) -> Explorer:
    qry = """UPDATE explorer
            SET country=:country,
                name=:name,
                description=:description
            WHERE   name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(f"Explorer with name '{explorer.name}' not found.")

def replace(explorer: Explorer) -> Explorer:
    return explorer

def delete(explorer: Explorer) -> Optional[bool]:
    qry = "delete from explorer where name=:name"
    params = {"name":explorer.name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return True
    else:
        raise Missing(f"Explorer with name '{explorer.name}' not found.")