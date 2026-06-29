from pydantic import BaseModel, field_validator, EmailStr

class createUser(BaseModel):
    username:str
    password:str
    @field_validator('password')
    def validate_password(cls, value):
        if len(value)<8:
            raise ValueError("Password must be at least 8 character length")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in value):
            raise ValueError("Passwod must contain at least one Upper Case Letter")
        return value