from model.explorer import Explorer

# fake data will be replaced
_explorers = [
    Explorer(name="Santosh Jami", country= "India", description="Love Movies"),
    Explorer(name="Sai Sashruth Jami", country= "India", description="Love Mom"),
    Explorer(name="Sruthi Sasanapuri", country= "India", description="Love Work")
]

def get_all()-> list[Explorer]:
    """return all exploreres"""
    return _explorers

def get_one(name:str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name==name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """Add an Explorer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """ Modify Explorer"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """ Replace Explorer"""
    return explorer

def delete(explorer: Explorer) -> bool | None:
    """ Delete Explorer"""
    return None
