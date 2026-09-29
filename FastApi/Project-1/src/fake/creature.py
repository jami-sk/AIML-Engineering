from src.model.creature import Creature

# fake data will be replaced
_creatures = [
    Creature(name="Yeti", country= "India", area="Himalayas", description="Love Movies",aka="Abominable Snowman"),
    Creature(name="Big Foot", area="Himalayas", aka="Love Movies", country= "India", description="Yeti's Cousin Yeddi")
]

def get_all()-> list[Creature]:
    """return all creaturees"""
    return _creatures

def get_one(name:str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name==name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """Add an creature"""
    return creature

def modify(creature: Creature) -> Creature:
    """ Modify creature"""
    return creature

def replace(creature: Creature) -> Creature:
    """ Replace creature"""
    return creature

def delete(name: str) -> bool | None:
    """ Delete creature"""
    return None
