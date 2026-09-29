class Missing(Exception):
    """Raised when a required value is missing."""
    def __init__(self, message:str="A required value is missing."):
        self.msg = message

class Duplicate(Exception):
    """Raised when a duplicate value is found."""
    def __init__(self, message:str="A duplicate value was found."):
        self.msg = message