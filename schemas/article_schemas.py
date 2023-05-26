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