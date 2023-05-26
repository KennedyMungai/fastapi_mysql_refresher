"""The file to hold the article schemas"""
import email
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ArticleBase(BaseModel):
    """The base schema for the articles

    Args:
        BaseModel (Pydantic): The base schema for the articles
    """
    title: str
    body: Optional[str] = None


class ArticleCreate(ArticleBase):
    """The schema for creating articles

    Args:
        ArticleBase (Pydantic): The base schema for the articles
    """
    pass


class Article(ArticleBase):
    """The model for the db data

    Args:
        ArticleBase (Base Article class): The base for all Article Schemas
    """
    id: int
    author: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        """The config for the model"""
        orm_mode = True


class ArticleUpdate(BaseModel):
    """The schema for updating articles

    Args:
        BaseModel (Pydantic): The base schema for the articles
    """
    title: Optional[str] = None
    body: Optional[str] = None

    class Config:
        """The config for the model"""
        orm_mode = True
