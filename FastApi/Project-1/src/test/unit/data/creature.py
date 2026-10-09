import os
import pytest
from model.creature import Creature
from error import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name = "Yeti",
        country = "CN",
        area = "Himalayas",
        description= "Hirsute Himalayan",
        aka = "Adominable Snowman")

def test_create(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample

def test_create_duplicate(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample
    with pytest.raises(Duplicate):
        creature.create(sample)

def test_get_one(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample
    resp = creature.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        creature.get_one("NonExistentCreature")

def test_modify(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample
    modified = Creature(
        name = "Yeti",
        country = "CN",
        area = "Himalayas",
        description= "Modified Description",
        aka = "Adominable Snowman")
    resp = creature.modify(sample.name, modified)
    assert resp == sample

def test_modify_missing():
    with pytest.raises(Missing):
        creature.modify("NonExistentCreature", sample)

def test_delete(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample
    result = creature.delete(sample.name)
    assert result is None

def test_delete_missing():
    with pytest.raises(Missing):
        creature.delete("NonExistentCreature")