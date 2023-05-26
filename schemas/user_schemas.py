"""Created the Schema file for the Users"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """The base model for the users

    Args:
        BaseModel (Pydantic): The parent class for the Models
    """
    email: EmailStr
    
    
class UserCreate(UserBase):
    """The model for the user creation

    Args:
        UserBase (UserBase): The parent class for the models
    """
    password: str