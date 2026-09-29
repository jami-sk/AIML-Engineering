from src.data import conn, curs
from src.model.creature import Creature
from typing import Optional

curs.execute("""CREATE TABLE if not exists creature(
             name text primary key,
             description text,
             country text, 
             area text,
             aka text)""")

def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name=name, description=description, country=country, area=area, aka=aka)

def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()

def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature) -> Creature:
    qry = """insert into creature values (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    curs.execute(qry, params)
    return get_one(creature.name)

def modify(creature: Creature) -> Creature:
    qry = """UPDATE creature
            SET country=:country,
                name=:name,
                description=:description,
                are=:area,
                aka=:aka
            WHERE   name=:name_orig"""
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(qry, params)
    return get_one(creature.name)

def replace(creature: Creature) -> Creature:
    return creature

def delete(creature: Creature) -> Optional[bool]:
    qry = "delete from creature where name=:name"
    params = {"name":creature.name}
    res = curs.execute(qry, params)
    return bool(res)