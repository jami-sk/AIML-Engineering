from fastapi import HTTPException
import pytest
import os
os.environ["CRYPTID_UNIT_TEST"] = True
from model.creature import Creature
from web import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(name="Dragon", description="A mythical creature", habitat="Mountains")

@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()

def assert_duplicate(exc):
    assert isinstance(exc, HTTPException)
    assert exc.status_code == 404
    assert "Duplicate" in exc.msg

def assert_missing(exc):
    assert isinstance(exc, HTTPException)
    assert exc.status_code == 404
    assert "Missing" in exc.msg

def test_create(sample: Creature):
    created = creature.create(sample)
    assert created == sample

def test_create_duplicate(sample: Creature):
    with pytest.raises(HTTPException) as exc:
        creature.create(fakes[0])
    assert_duplicate(exc.value)

def test_get_one(sample: Creature):
    fetched = creature.get_one(fakes[0].name)
    assert fetched == fakes[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        creature.get_one("NonExistentCreature")
    assert_missing(exc.value)

def test_modify(sample: Creature):
    modified = creature.modify(fakes[0].name, fakes[0])
    assert modified == fakes[0]

def test_modify_missing():
    with pytest.raises(HTTPException) as exc:
        creature.modify("NonExistentCreature", Creature(name="NewName", description="NewDesc", habitat="NewHabitat"))
    assert_missing(exc.value)

def test_delete():
    result = creature.delete(fakes[0].name)
    assert result is None

def test_delete_missing():
    with pytest.raises(HTTPException) as exc:
        creature.delete("NonExistentCreature")
    assert_missing(exc.value)