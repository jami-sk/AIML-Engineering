from src.model.creature import Creature
from src.service import creature as code
import os, pytest
os.environ["CRYPTID_UNIT_TEST"] = True
from error import Duplicate, Missing

@pytest.fixture
def sample() -> Creature:
    return Creature(
        name = "Yeti",
        country = "CN",
        area = "Himalayas",
        description= "Hirsute Himalayan",
        aka = "Adominable Snowman")

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_create_duplicate():
    resp = code.create(sample)
    assert resp == sample
    with pytest.raises(Duplicate):
        resp = code.create(sample)

def test_get_exists():
    resp = code.create(sample)
    assert resp == sample
    resp = code.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    with pytest.raises(Missing):
        _ = code.get_one("NonExistentCreature")

def test_modify(sample):
    resp = code.create(sample)
    assert resp == sample
    modified = Creature(
        name = "Yeti",
        country = "CN",
        area = "Himalayas",
        description= "Modified Description",
        aka = "Adominable Snowman")
    resp = code.modify(sample.name, modified)
    assert resp == sample

def test_modify_missing():
    bob: Creature = Creature(
        name = "Bob",
        country = "US",
        area = "Alaska",
        description= "A fictional creature",
        aka = "Bigfoot")
    with pytest.raises(Missing):
        _ = code.modify("NonExistentCreature", bob)
