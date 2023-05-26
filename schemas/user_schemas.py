"""Created the Schema file for the Users"""
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.article_schemas import Article


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


class User(UserBase):
    """The User Model

    Args:
        UserBase (Pydantic): The parent class for the models
    """
    id: int
    is_active: bool
    articles: List[Article]

    class Config:
        """The config class"""
        orm_mode = True
